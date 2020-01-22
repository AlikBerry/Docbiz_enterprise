from django.contrib import admin
from .models import *
from daterange_filter.filter import DateRangeFilter


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Transactions._meta.fields]
    list_filter = (('created_date', DateRangeFilter),)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Menu._meta.fields]


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Clients._meta.fields]
    search_fields = ["address", "city", "type_of_activity"]


@admin.register(ClientsPayment)
class ClientsPaymentAdmin(admin.ModelAdmin):
    list_display =  [f.name for f in ClientsPayment._meta.fields]
    autocomplete_fields = ["client"]

@admin.register(Cashboxes)
class CashboxesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Cashboxes._meta.fields]
    search_fields = ["number_of_cashbox", "client__address", "client__city", "iep__iep_name"]
    autocomplete_fields = ["client", "iep"]

@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Terminal._meta.fields]
    search_fields = ["number_of_terminal", "client__city", "client__address", "iep__iep_name"]
    autocomplete_fields = ["client", "iep"]



class IepInfoTabularInline(admin.TabularInline):
    model = IndividualEntrepreneurInfo
    extra = 0

@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndividualEntrepreneur._meta.fields]
    inlines = [IepInfoTabularInline]
    search_fields = ["iep_name"]

class EmployeeSalaryTabularInline(admin.TabularInline):
    model = EmployeeSalary
    extra = 0

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Employee._meta.fields]
    inlines = [EmployeeSalaryTabularInline]



@admin.register(IndividualEntrepreneurSalary)
class IndividualEntrepreneurSalaryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndividualEntrepreneurSalary._meta.fields]
    autocomplete_fields = ["iep"]


@admin.register(IndividualEntrepreneurDebt)
class IndividualEntrepreneurDebtAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndividualEntrepreneurDebt._meta.fields]
    autocomplete_fields = ["iep"]