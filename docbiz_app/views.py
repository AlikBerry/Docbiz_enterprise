from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import request
from search_views.filters import BaseFilter
from search_views.search import SearchListView

from docbiz_app.forms import LoginForm, TransactionForm


from .models import Cashboxes, Clients, Employee, Menu, Terminal, Transactions


def login_page_data():
    return {
        "login_form": LoginForm(),
        "menu_list": Menu.objects.all()
    }


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

@login_required(login_url="/login")
def table_trans(request):
    if request.user.is_superuser:
        context = login_page_data()
        context['transactions'] = Transactions.objects.all().order_by('created_date')
        paginator = Paginator(context['transactions'], 100)
        page = request.GET.get('page')
        context['transactions'] = paginator.get_page(page)
        context['sum_incoming'] = ''.join(f'{v}' for k, v in Transactions.objects.aggregate(Sum('incoming')).items())
        context['sum_expense'] = ''.join(f'{v}' for k, v in Transactions.objects.aggregate(Sum('expense')).items())
        context['balance'] = ''.join(f'{v}' for k, v in Transactions.objects.aggregate(Sum('balance')).items())
    
        ''' After code is filtering user queryset '''

    if  request.GET.get('start_date') and request.GET.get('end_date'):
            start_date = request.GET.get('start_date')
            end_date = request.GET.get('end_date')
            context['queryset'] = Transactions.objects.filter(created_date__range=(start_date, end_date)).order_by('created_date')
            context['sum_incoming'] = ''.join(f'{v}' for k, v in context['queryset'].aggregate(Sum('incoming')).items())
            context['sum_expense'] = ''.join(f'{v}' for k, v in context['queryset'].aggregate(Sum('expense')).items())
            context['balance'] = ''.join(f'{v}' for k, v in context['queryset'].aggregate(Sum('balance')).items())
            if not context['queryset']:
                context = login_page_data()
                return render(request, "table_transaction.html", context)  
            return render(request, "table_transaction.html", context)
        
    if request.GET.get('description'):
            description = request.GET.get('description')
            context['queryset_1'] = Transactions.objects.filter(description__icontains=description)
            context['sum_incoming'] = ''.join(f'{v}' for k, v in context['queryset_1'].aggregate(Sum('incoming')).items())
            context['sum_expense'] = ''.join(f'{v}' for k, v in context['queryset_1'].aggregate(Sum('expense')).items())
            context['balance'] = ''.join(f'{v}' for k, v in context['queryset_1'].aggregate(Sum('balance')).items())
            if not context['queryset_1']:
                context = login_page_data()
                return render(request, "table_transaction.html", context)
            return render(request, "table_transaction.html", context)
    return render(request, "table_transaction.html", context)

    



@login_required(login_url="/login")
def employee(request):
   context = login_page_data()
   context['employee'] = Employee.objects.all()
   return render(request, 'table_employee.html', context)


@login_required(login_url="/login")
def clients(request):
    context = login_page_data()
    context['clients'] = Clients.objects.all()
    paginator = Paginator(context['clients'], 70)
    page = request.GET.get('page')
    context['clients'] = paginator.get_page(page)

    ''' After code is filtering user queryset '''

    if  request.GET.get('start_date') and request.GET.get('end_date'):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        context['queryset'] = Clients.objects.filter(created_date__range=(start_date, end_date))
        if not context['queryset']:
            context = login_page_data()
            return render(request, 'table_clients.html', context)
        return render(request, 'table_clients.html', context)
    if request.GET.get('city') or request.GET.get('address') or request.GET.get('type_of_activity'):
        city = request.GET.get('city')
        address = request.GET.get('address')
        type_of_activity = request.GET.get('type_of_activity')
        context['queryset_1'] = Clients.objects.filter(Q(city=city) | Q(address=address))
        return render(request, 'table_clients.html', context)
    if request.GET.get('type_of_activity'):
        type_of_activity = request.GET.get('type_of_activity')
        context['queryset_1'] = Clients.objects.filter(Q(city__icontains=city) &
         Q(address__icontains=address) & 
         Q(type_of_activity__icontains=type_of_activity))
        if not context['queryset_1']:
            context = login_page_data()
            return render(request, 'table_clients.html', context)
        return render(request, 'table_clients.html', context)
    return render(request, 'table_clients.html', context)

    
    

@login_required(login_url="/login")
def cashboxes(request):
    context = login_page_data()
    context['cashboxes'] = Cashboxes.objects.all()
    paginator = Paginator(context['cashboxes'], 70)
    page = request.GET.get('page')
    context['cashboxes'] = paginator.get_page(page)

    ''' After code is filtering user queryset '''

    if request.GET.get('created_date') or request.GET.get('model_name') or request.GET.get('number_of_cashbox') or request.GET.get('iep') or request.GET.get('client'):
        created_date = request.GET.get('created_date')
        model_name = request.GET.get('model_name')
        number_of_cashbox = request.GET.get('number_of_cashbox')
        iep = request.GET.get('iep')
        client = request.GET.get('client')
        context['queryset'] = Cashboxes.objects.filter(Q(created_date__contains=created_date) & 
        Q(model_name__icontains=model_name) & 
        Q(number_of_cashbox__icontains=number_of_cashbox) & 
        Q(iep__iep_name__icontains=iep) & 
        Q(client__address__icontains=client))
        print(context['queryset'])
        if not context['queryset']:
            context = login_page_data()
            return render(request, 'table_cashbox.html', context)
        return render(request, 'table_cashbox.html', context)
    return render(request, 'table_cashbox.html', context)

@login_required(login_url="/login")
def cashboxes_detail(request, id):
    context = login_page_data()
    if id is None:
        return render(request, 'table_clients.html', context)
    my_clients = Clients.objects.get(id=id)
    cashboxes_list = []
    for i  in  my_clients.cashbox.all():
        cashboxes_list.append({
            "created_date":i.created_date,
            "model_name":i.model_name,
            "number_of_cashbox":i.number_of_cashbox,
            "iep":i.iep,
            "client":i.client
        })

    context = login_page_data()
    context["cashbox_detail"] = cashboxes_list
    return  render(request, 'table_cashbox.html', context)


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
    

@login_required(login_url="/login")
def terminals(request):
    context = login_page_data()
    context['terminals'] = Terminal.objects.all()
    paginator = Paginator(context['terminals'], 70)
    page = request.GET.get('page')
    context['terminals'] = paginator.get_page(page)

    ''' After code is filtering user queryset '''

    if request.GET.get('created_date') or request.GET.get('number_of_terminal') or request.GET.get('iep') or request.GET.get('client'):
        created_date = request.GET.get('created_date')
        number_of_terminal = request.GET.get('number_of_terminal')
        iep = request.GET.get('iep')
        client = request.GET.get('client')
        context['queryset'] = Terminal.objects.filter(Q(created_date__contains=created_date) & 
        Q(number_of_terminal__icontains=number_of_terminal) & 
        Q(iep__iep_name__icontains=iep) & 
        Q(client__address__icontains=client) |
        Q(created_date__contains=created_date) & 
        Q(number_of_terminal__icontains=number_of_terminal) & 
        Q(iep__iep_name__icontains=iep) &                                               
        Q(client__address__isnull=True))
        if not context['queryset']:
            context = login_page_data()
            return render(request, 'table_terminal.html', context)
        return render(request, 'table_terminal.html', context)
    return render(request, 'table_terminal.html', context)


    return render(request, 'table_terminal.html', context)

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



