from django.conf import settings
from django.conf.urls.static import static

from . import  views
from django.urls import path

urlpatterns = [
  
    path("", views.baseindexview, name='home'),
    path("login/", views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("base/", views.base, name='base'),
    path("table_iep/", views.IndividualEntrepreneurTableView, name='iep_table'),
    path("table_trans/", views.TableTransactionView, name='table_trans'),
    path("table_clients/", views.ClientsView, name='table_clients'),
    path("table_cashboxes/", views.CashboxesView, name='cashboxes'),
    path("transaction_form/", views.add_transaction, name='add_transaction'),
    path("table_trans/<int:id>/update", views.update_transaction, name='update_transaction'),
    path("table_trans/<int:id>/delete", views.delete_transaction, name='delete_transaction'),
    path("table_cashboxes/<int:id>", views.cashboxes_detail, name='cashboxes_detail'),
    path("table_terminals/<int:id>", views.terminals_detail, name='terminals_detail'),
    

]

