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
    search_fields = ('number_of_cashbox',)

    def queryset(self, request, queryset):
        if self.value() is not None:
            uid = self.value()
            return queryset.filter(
                Q(uid=uid) |
                Q(payment__uid=uid) |
                Q(user__uid=uid)
            )

@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Terminal._meta.fields]

@admin.register(IndividualEntrepreneur)
class IepsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndividualEntrepreneur._meta.fields]


@admin.register(IndividualEntrepreneurInfo)
class IepsInfoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndividualEntrepreneurInfo._meta.fields]



