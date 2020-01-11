from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Sum, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import request
from search_views.filters import BaseFilter
from search_views.search import SearchListView
from docbiz_app.forms import LoginForm, TransactionForm
from .models import Cashboxes, Clients, Employee, Menu, Terminal, Transactions
from django.core import paginator
from docbiz_app.models import IndividualEntrepreneur


def login_page_data():
    context = {
        "login_form": LoginForm(),
        "menu_list": Menu.objects.all()
    }
    return context

def baseindexview(request):
    if request.user.is_authenticated:
        return redirect("base")
    context = login_page_data()
    return render(request, "login.html", context)

def login_view(request):
    if request.method == "POST":
        context = login_page_data()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect("base")
            else:
                context["message"] = "имя пользователя или пароль неверен!"
                return render(request, "login.html", context)
        else:
            context["login_form"] = form
            return render(request, "login.html", context)
    else:
        return redirect("home")

        
def logout_view(request):
    logout(request)
    return redirect("home")

@login_required(login_url="/login")
def base(request):
    context = login_page_data()
    return render(request, "base.html", context)

def is_valid_queryparam(param):
    return param != '' and param is not None

@login_required(login_url='/login')
def TableTransactionView(request):
    if request.user.is_superuser:
        qs = Transactions.objects.all()
        description = request.GET.get('description')
        min_incoming = request.GET.get('min_incoming')
        max_incoming = request.GET.get('max_incoming')
        min_created_date = request.GET.get('min_created_date')
        max_created_date = request.GET.get('max_created_date')
        if is_valid_queryparam(description):
            qs = qs.filter(description__icontains=description)
        if is_valid_queryparam(min_incoming) and is_valid_queryparam(max_incoming):
            qs = qs.filter(incoming__range=(min_incoming, max_incoming))
        if is_valid_queryparam(min_created_date) and is_valid_queryparam(max_created_date):
            qs = qs.filter(created_date__range=(min_created_date, max_created_date))
        
        paginator = Paginator(qs, 100)
        page = request.GET.get('page')
        qs = paginator.get_page(page)

        context = {
            'queryset': qs,
            'menu_list': Menu.objects.all()
        }

        context['sum_incoming'] = ''.join(f'{v}' for k, v in Transactions.objects.aggregate(Sum('incoming')).items())
        context['sum_expense'] = ''.join(f'{v}' for k, v in Transactions.objects.aggregate(Sum('expense')).items())
        context['balance'] = ''.join(f'{v}' for k, v in Transactions.objects.aggregate(Sum('balance')).items())

    return render(request, 'table_transaction.html', context)

    

@login_required(login_url='/login')
def ClientsView(request):
    qs = Clients.objects.all()
    city = request.GET.get('city')
    address = request.GET.get('address')
    type_of_activity = request.GET.get('type_of_activity')
    contacts = request.GET.get('contacts')
    payment = request.GET.get('payment')
    if is_valid_queryparam(city):
        qs = qs.filter(city__icontains=city)
    if is_valid_queryparam(address):
        qs = qs.filter(address__icontains=address)
    if is_valid_queryparam(type_of_activity):
        qs = qs.filter(type_of_activity__icontains=type_of_activity)
    if is_valid_queryparam(contacts):
        qs = qs.filter(contacts__icontains=contacts)
    if is_valid_queryparam(payment):
        qs = qs.filter(payment=payment)
    
    paginator = Paginator(qs, 100)
    page = request.GET.get('page')
    qs = paginator.get_page(page)

    context = {
        'queryset': qs,
        'menu_list': Menu.objects.all()
    }

    return render(request, 'table_clients.html', context)


@login_required(login_url='/login')
def CashboxesView(request):
    qs = Cashboxes.objects.all()
    qs1 = Clients.objects.all()
    min_created_date = request.GET.get('min_created_date')
    max_created_date = request.GET.get('max_created_date')
    model_name = request.GET.get('model_name')
    number_of_cashbox = request.GET.get('number_of_cashbox')
    iep = request.GET.get('iep')
    client = request.GET.get('client')
    type_of_activity = request.GET.get('type_of_activity')
    if is_valid_queryparam(min_created_date) and is_valid_queryparam(max_created_date):
        qs = qs.filter(created_date__range=(min_created_date, max_created_date))
    if is_valid_queryparam(model_name):
        qs = qs.filter(model_name__icontains=model_name)
    if is_valid_queryparam(number_of_cashbox):
        qs = qs.filter(number_of_cashbox__icontains=number_of_cashbox)
    if is_valid_queryparam(iep):
        qs = qs.filter(iep__iep_name__icontains=iep)
    if is_valid_queryparam(client):
        qs = qs.filter(Q(client__address__icontains=client) | Q(client__city=client))
    if is_valid_queryparam(type_of_activity):
        qs = qs.filter(client__type_of_activity__icontains=type_of_activity)

    paginator = Paginator(qs, 150)
    page = request.GET.get('page')
    qs = paginator.get_page(page)

    context = {
        'queryset': qs,
        'queryset_1': qs1,
        'menu_list': Menu.objects.all()
    }

    return render(request, 'table_cashbox.html', context)

@login_required(login_url="/login")
def IndividualEntrepreneurTableView(request):
    qs = IndividualEntrepreneur.objects.all()
    iep_name = request.GET.get('iep_name')
    if is_valid_queryparam(iep_name):
        qs = qs.filter(iep_name__icontains=iep_name)
    
    paginator = Paginator(qs, 100)
    page = request.GET.get('page')
    qs = paginator.get_page(page)

    context = {
        'queryset': qs,
        'menu_list': Menu.objects.all()
    }

    return render(request, 'table_iep.html', context)
    

@login_required(login_url="/login")
def cashboxes_detail(request, id):
    context = login_page_data()
    if id is None:
        return render(request, 'table_clients.html', context)
    my_clients = Clients.objects.get(id=id)
    qs1 = IndividualEntrepreneur.objects.all()
    cashboxes_list = []
    for i  in  my_clients.cashbox.all():
        cashboxes_list.append({
            "created_date":i.created_date,
            "model_name":i.model_name,
            "number_of_cashbox":i.number_of_cashbox,
            "iep":i.iep,
            "client":i.client
        })

    context = {
        'cashbox_detail': cashboxes_list,
        'qs1': qs1,
        'menu_list': Menu.objects.all()
    }
    return  render(request, 'table_cashbox.html', context)

@login_required(login_url="/login")
def terminals_detail(request, id):
    context = login_page_data()
    if id is None:
        return render(request, 'table_clients.html', context)
    my_clients = Clients.objects.get(id=id)
    terminals_list = []
    for i  in  my_clients.terminal.all():
        terminals_list.append({
            "created_date": i.created_date,
            "number_of_terminal": i.number_of_terminal,
            "iep": i.iep,
            "client": i.client
        })

    context = login_page_data()
    context["terminal_detail"] = terminals_list
    return  render(request, 'table_terminal.html', context)

@login_required(login_url="/login")
def add_transaction(request):
    context = login_page_data()
    if request.method == 'POST':
       form = TransactionForm(request.POST)
       if form.is_valid():
           created_date = request.POST.get('created_date')
           incoming = request.POST.get('incoming')
           expense = request.POST.get('expense')
           description = request.POST.get('description')
           trans = Transactions.objects.create(created_date=created_date, incoming=int(incoming), expense=int(expense), description=description)
           return redirect('table_trans')
    return render(request, 'transaction_form.html', context)

@login_required(login_url="/login")
def update_transaction(request, id):
    context = login_page_data()
    transaction = Transactions.objects.get(id=id)
    form = TransactionForm(request.POST, instance = transaction)
    if form.is_valid():  
        form.save()  
        return redirect("/table_trans")
    return render(request, 'update_transaction_form.html', {'transaction': transaction})  

@login_required(login_url="/login")
def delete_transaction(request, id):
    context = login_page_data()
    transaction = Transactions.objects.get(id=id) 
    if transaction:
        if request.method == 'POST':
            transaction.delete()  
            return redirect('table_trans')
        context['transaction'] = transaction
        return render(request, 'confirm.html', context)
    return redirect("table_trans")  
    





