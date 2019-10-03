from django.conf import settings
from django.conf.urls.static import static

from . import  views
from django.urls import path

urlpatterns = [
    path("", views.baseindexview, name='home'),
    path("login/", views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("base/", views.base, name='base'),
    path("table_trans/", views.table_trans, name='table_trans'),
    path("table_employee/", views.employee, name='emp_salary'),
    path("table_clients/", views.clients, name='clients'),
    path("table_cashboxes/", views.cashboxes, name='cashboxes'),
    path("table_terminals/", views.terminals, name='terminals'),
    path("add_trans/", views.add_transactions, name='add_transaction'),
    path("table_cashboxes/<int:id>", views.cashboxes_detail, name='cashboxes_detail'),
    path("table_terminals/<int:id>", views.terminals_detail, name='terminals_detail')

]

