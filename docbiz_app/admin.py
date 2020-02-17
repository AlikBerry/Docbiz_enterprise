from django.contrib import admin
from .models import *
from daterange_filter.filter import DateRangeFilter


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ["created_date", "incoming", "expense", "description"]
    list_filter = (('created_date', DateRangeFilter),)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Menu._meta.fields]


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ["address", "city", "type_of_activity", "landlord", "contacts", "payment"]
    search_fields = ["address", "city", "type_of_activity", "landlord"]


@admin.register(ClientsPayment)
class ClientsPaymentAdmin(admin.ModelAdmin):
    list_display =  ["client", "description", "amount"]
    autocomplete_fields = ["client"]
    search_fields= ["client__address", "client__city"]
    list_filter = (('created_date', DateRangeFilter),)



@admin.register(Cashboxes)
class CashboxesAdmin(admin.ModelAdmin):
    list_display = ["number_of_cashbox", "model_name", "iep", "client"]
    search_fields = ["number_of_cashbox", "client__address", "client__city", "iep__iep_name", "iep__type_of_activity"]
    autocomplete_fields = ["client", "iep"]

@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    list_display = ["number_of_terminal", "created_date", "iep", "client"]
    search_fields = ["number_of_terminal", "client__city", "client__address", "iep__iep_name", "iep__type_of_activity"]
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
    list_display = ["full_name"]
    inlines = [EmployeeSalaryTabularInline]



@admin.register(IndividualEntrepreneurSalary)
class IndividualEntrepreneurSalaryAdmin(admin.ModelAdmin):
    list_display = ["iep", "created_date", "description", "amount"]
    autocomplete_fields = ["iep"]
    list_filter = (('created_date', DateRangeFilter),)



@admin.register(IndividualEntrepreneurDebt)
class IndividualEntrepreneurDebtAdmin(admin.ModelAdmin):
    list_display = ["iep", "update_date", "description", "debt"]
    autocomplete_fields = ["iep"]