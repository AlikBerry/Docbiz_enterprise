from django.contrib import admin
from .models import Transactions, Menu, Employee, Clients, Cashboxes, IndividualEntrepreneur, IndividualEntrepreneurInfo, \
    Terminal
from daterange_filter.filter import DateRangeFilter


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'incoming', 'expense', 'description')
    list_filter = (('created_date', DateRangeFilter),)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'type_of_activity', 'status', 'id')

@admin.register(Cashboxes)
class CashboxesAdmin(admin.ModelAdmin):
    list_display = ('number_of_cashbox', 'model_name', 'iep', 'client', 'id')
  


@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    list_display = ('number_of_terminal', 'iep', 'client', 'id')

@admin.register(IndividualEntrepreneur)
class IepsAdmin(admin.ModelAdmin):
    list_display = ('iep_name', 'tel_number', 'el_key', 'status', 'id' )


@admin.register(IndividualEntrepreneurInfo)
class IepsInfoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndividualEntrepreneurInfo._meta.fields]



