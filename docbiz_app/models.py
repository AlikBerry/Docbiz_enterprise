from django.db import models
from django.db.models import Sum

from docbiz import settings


class Menu(models.Model):
    name = models.CharField(max_length=155)
    url = models.CharField(max_length=155)
    order = models.IntegerField()

    def __str__(self):
        return "{}{}".format('name', 'url')

    class Meta:
        ordering = ['order']

class Transactions(models.Model):

    CATEGORY_TRANSACTION = (
        ('Расходы ДокБиз','Расходы ДокБиз'),
        ('Расходы Реальные','Расходы Реальные'),
    )

    date_pub = models.DateField(auto_now=False, auto_created=False)
    date_up = models.DateField(auto_now=True, auto_now_add=False)
    incoming = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    expense = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=CATEGORY_TRANSACTION, null=True, blank=True)



    def get_balance(self):
        return self.incoming - self.expense


    class Meta:
        verbose_name = 'Transactions'
        verbose_name_plural = 'Transactions'


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    tel_num = models.CharField(max_length=155)
    address = models.CharField(max_length=255)
    job = models.CharField(max_length=155)




