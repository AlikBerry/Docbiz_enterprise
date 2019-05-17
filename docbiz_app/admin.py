from django.contrib import admin
from .models import Transactions, Menu


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_pub', 'date_up', 'incoming', 'expense', 'description')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order')
