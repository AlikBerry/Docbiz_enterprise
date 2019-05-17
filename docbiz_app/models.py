from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=155)
    url = models.CharField(max_length=155)
    order = models.IntegerField()

    def __str__(self):
        return "{}{}".format('name', 'url')

    class Meta:
        ordering = ['order']

class Transactions(models.Model):
    date_pub = models.DateTimeField(auto_created=True)
    date_up = models.DateTimeField(auto_now=True)
    incoming = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    expense = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    description = models.CharField(max_length=255)


    def get_balance(self):
        return self.incoming - self.expense



    class Meta:
        verbose_name = 'Transactions'
        verbose_name_plural = 'Transactions'


