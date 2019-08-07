from django.contrib import admin
from .models import Transactions, Menu, Employee, Clients, Cashboxes, IndividualEntrepreneur, IndividualEntrepreneurInfo, \
    Terminal


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Transactions._meta.fields]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Menu._meta.fields]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Employee._meta.fields]

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Clients._meta.fields]

@admin.register(Cashboxes)
class CashboxesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Cashboxes._meta.fields]

@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Terminal._meta.fields]

@admin.register(IndividualEntrepreneur)
class IepsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndividualEntrepreneur._meta.fields]


@admin.register(IndividualEntrepreneurInfo)
class IepsInfoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndividualEntrepreneurInfo._meta.fields]



