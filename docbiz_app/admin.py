from django.contrib import admin
from .models import *
from daterange_filter.filter import DateRangeFilter






@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ["created_date", "incoming", "expense", "balance", "description"]
    list_filter = (('created_date', DateRangeFilter),)
    search_fields = ["description"]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Menu._meta.fields]


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ["address", "city", "type_of_activity", "landlord", "contacts", "payment"]
    search_fields = ["address", "city", "type_of_activity", "landlord"]
    


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

class IepSalaryTabularInline(admin.TabularInline):
    model = IndividualEntrepreneurSalary
    extra = 0

@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ["iep_name", "ident_number", "type_of_activity", "el_key", "status", "sign", "created_date"]
    inlines = [IepInfoTabularInline, IepSalaryTabularInline]
    search_fields = ["iep_name"]



class EmployeeSalaryTabularInline(admin.TabularInline):
    model = EmployeeSalary
    extra = 0

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["full_name"]
    inlines = [EmployeeSalaryTabularInline]
