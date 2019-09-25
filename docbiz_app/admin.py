from django.contrib import admin
from .models import Transactions, Menu, Employee, Clients, Cashboxes, IndividualEntrepreneur, \
    IndividualEntrepreneurInfo, Terminal
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
    search_fields = ["address", "city", "type_of_activity"]

@admin.register(Cashboxes)
class CashboxesAdmin(admin.ModelAdmin):
    list_display = ('number_of_cashbox', 'model_name', 'iep', 'client', 'id')
    search_fields = ["number_of_cashbox", "client__address", "client__city", "iep__iep_name"]
    autocomplete_fields = ["client", "iep"]

@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    list_display = ('number_of_terminal', 'iep', 'client', 'id')
    search_fields = ["number_of_terminal", "client__city", "client__address", "iep__iep_name"]
    autocomplete_fields = ["client", "iep"]



class IepInfoTabularInline(admin.TabularInline):
    model = IndividualEntrepreneurInfo
    extra = 1

@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    inlines = [IepInfoTabularInline]
    search_fields = ["iep_name"]



# @admin.register(IndividualEntrepreneur)
# class IepsAdmin(admin.ModelAdmin):
#     list_display = ('iep_name', 'created_date', 'tel_number', 'el_key', 'status', 'id' )
#     search_fields = ["iep_name"]
#
#
#
# @admin.register(IndividualEntrepreneurInfo)
# class IepsInfoAdmin(admin.ModelAdmin):
#     list_display = ('iep', 'bank', 'login', 'password', 'codeword', 'password_of_card')
#     autocomplete_fields = ["iep"]




