from decimal import Decimal
from unicodedata import decimal
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from docbiz_app.forms import LoginForm
from .models import Transactions, Menu, Employee, Clients, Cashboxes, Terminal


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

@login_required(login_url="/login")
def base(request):
    context = login_page_data()
    return render(request, "base.html", context)

@login_required(login_url="/login")
def table_trans(request):
    if request.user.is_superuser:
        context = login_page_data()
        context['transactions'] = Transactions.objects.all().order_by('created_date')
        paginator = Paginator(context['transactions'], 20)
        page = request.GET.get('page')
        context['transactions'] = paginator.get_page(page)
        context['sum_incoming'] = Transactions.objects.aggregate(Sum('incoming'))
        context['sum_incoming'] = ''.join('{}'.format(val) for key, val in context['sum_incoming'].items())
        context['sum_expense'] = Transactions.objects.aggregate(Sum('expense'))
        context['sum_expense'] = ''.join('{}'.format(val) for key, val in context['sum_expense'].items())
        context['balance'] = format(float(context['sum_incoming'])-float(context['sum_expense']), '.2f')

        return render(request, 'table_transaction.html', context)
    else:
        context = login_page_data()
        return render(request, 'base.html', context)

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required(login_url="/login")
def employee(request):
   context = login_page_data()
   context['employee'] = Employee.objects.all()
   return render(request, 'table_employee.html', context)

@login_required(login_url="/login")
def clients(request):
    context = login_page_data()
    context['clients'] = Clients.objects.filter(status=True)
    return render(request, 'table_clients.html', context)

@login_required(login_url="/login")
def cashboxes(request):
    context = login_page_data()
    context['cashboxes'] = Cashboxes.objects.all()
    return render(request, 'table_cashbox.html', context)

@login_required(login_url="/login")
def add_transactions(request):
    context = login_page_data()
    return render(request, "add_transaction.html", context)