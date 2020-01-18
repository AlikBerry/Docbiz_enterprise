from datetime import *
from django.db import models
from django.db.models import Sum


class Menu(models.Model):
    name = models.CharField(max_length=155)
    url = models.CharField(max_length=155)
    order = models.IntegerField()

    def __str__(self):
        return "{}{}".format('name', 'url')

    class Meta:
        db_table = "menu"
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['order']

class Transactions(models.Model): 
    created_date = models.DateField(auto_now=False, auto_created=False, default=datetime.now, verbose_name='дата публикации')
    update_date = models.DateField(auto_now_add=True, verbose_name='дата обновления')
    incoming = models.IntegerField(blank=True, null=True, default=0, verbose_name='приход')
    expense = models.IntegerField(blank=True, null=True, default=0, verbose_name='расход')
    balance = models.IntegerField(default=0, blank=True, null=True, verbose_name='баланс')
    description = models.CharField(max_length=255, verbose_name='назначение')

    def save(self, *args, **kwargs):
        self.balance = self.incoming - self.expense
        super(Transactions, self).save(*args, **kwargs)

    class Meta:
        db_table = "transactions"
        verbose_name = 'Транзакции'
        verbose_name_plural = 'Транзакции'
        ordering = ['created_date']


class Employee(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Ф.И.О')
    tel_num = models.CharField(max_length=155, verbose_name='номер тел.')
    address = models.CharField(max_length=255, verbose_name='адрес')
    salary = models.IntegerField(default=0, verbose_name='ЗП')


    class Meta:
        db_table = "employee"
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'


class EmployeeSalary(models.Model):
    created_date = models.DateField(auto_now=False, auto_created=False, default=datetime.now, verbose_name='дата')
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, verbose_name='сотрудник')
    amount = models.IntegerField(default=0, blank=True, null=True, verbose_name='оплата')
    description = models.CharField(max_length=155, blank=True, null=True, verbose_name='коментарий')
   

    class Meta:
        db_table = "employee_salary"
        verbose_name = 'ЗП сотрудника'
        verbose_name_plural = 'ЗП сотрудника'



class Clients(models.Model):

    TYPE_ACTIVITY = (

        ('Жора', 'Жора'),
        ('Интернет-магазин', 'Интернет-магазин'),
        ('Стройматреиалы', 'Стройматериалы'),
        ('Хозяйственный', 'Хозяйственный'),
        ('Магазин', 'Магазин'),
        ('Одежда', 'Одежда'),
        ('Продукты', 'Продукты'),
        ('Ресторан', 'Ресторан'),
        ('Сервис', 'Сервис'),
        ('Салон красоты', 'Салон красоты'),
        ('СМЦ', 'СМЦ'),
        ('Цветочный ряд', 'Цветочный ряд'),
    )

    created_date = models.DateField(auto_now=False, auto_created=False, default=datetime.now, verbose_name='дата')
    update_date = models.DateField(auto_now_add=True, verbose_name='дата обновления')
    city = models.CharField(max_length=100, verbose_name='город', blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name='адрес')
    type_of_activity = models.CharField(max_length=50, choices=TYPE_ACTIVITY, blank=True, null=True, verbose_name='вид деятельности')
    landlord = models.CharField(max_length=255, blank=True, null=True, verbose_name='арендодатель')
    contacts = models.CharField(max_length=155, blank=True, null=True, verbose_name='контакты')
    payment = models.IntegerField(default=0, verbose_name='оплата')
    status = models.BooleanField(default=True, verbose_name='статус')

    def __str__(self):
        return "{}, {}".format(self.city, self.address)

    class Meta:
        db_table = "clients"
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'
    

class ClientsPayment(models.Model):
    created_date = models.DateField(auto_now=False, auto_created=False, default=datetime.now, verbose_name='дата')
    client = models.ForeignKey('Clients', on_delete=models.DO_NOTHING, verbose_name='клиент')
    description = models.CharField(max_length=155, blank=True, null=True, verbose_name='коментарий')
    amount = models.IntegerField(default=0, verbose_name='сумма')

    class Meta:
        db_table = "clients_payment"
        verbose_name = 'Оплата Клиента'
        verbose_name_plural = 'Оплата Клиента'



class Cashboxes(models.Model):
    created_date = models.DateField(auto_now=False, auto_created=False, default=datetime.now, verbose_name='дата постановки')
    update_date = models.DateField(auto_now_add=True, verbose_name='дата обновления')
    model_name = models.CharField(max_length=155, blank=True, null=True, verbose_name='название модели')
    number_of_cashbox = models.CharField(max_length=100, verbose_name='номер кассы')
    iep = models.ForeignKey('IndividualEntrepreneur', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='ИП')
    client = models.ForeignKey('Clients', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='cashbox', verbose_name='клиент')


    def __str__(self):
        return "{}     {}".format( self.model_name, self.number_of_cashbox)

    class Meta:
        db_table = "cashboxes"
        verbose_name = 'Кассы'
        verbose_name_plural = 'Кассы'

class Terminal(models.Model):
    created_date = models.DateField(auto_now=False, auto_created=False, default=datetime.now, verbose_name='дата постановки')
    update_date = models.DateField(auto_now_add=True, verbose_name='дата обновления')
    number_of_terminal = models.CharField(max_length=100, verbose_name='номер терминала')
    iep = models.ForeignKey('IndividualEntrepreneur', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='ИП')
    client = models.ForeignKey('Clients', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='terminal', verbose_name='клиент')

    class Meta:
        db_table = "terminals"
        verbose_name = "Терминалы"
        verbose_name_plural = "Терминалы"


class IndividualEntrepreneur(models.Model):
    TYPE_ACTIVITY = (

        ('Цветы', 'Цветы'),
        ('Цветы солдат', 'Цветы солдат'),
        ('СМЦ', 'СМЦ'),
        ('СМЦ солдат', 'СМЦ солдат'),
        ('Одиночка', 'Одиночка'),
        ('Одиночка солдат', 'Одиночка солдат'),
    )
    
    created_date = models.DateField(auto_now=False, auto_created=False, default=datetime.now, verbose_name='дата открытия')
    update_date = models.DateField(auto_now_add=True, verbose_name='дата обновления')
    iep_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='ИП')
    ident_number = models.CharField(max_length=12, blank=True, null=True, verbose_name='ИНН')
    type_of_activity = models.CharField(max_length=50, choices=TYPE_ACTIVITY, verbose_name='вид деятельности')
    tel_number = models.CharField(max_length=12, blank=True, null=True, default='+7', verbose_name='номер тел.')
    el_key = models.BooleanField(default=True, verbose_name='электронный ключ')
    status = models.BooleanField(default=True, verbose_name='статус')


    class Meta:
        db_table = "individual_entrepreneur"
        verbose_name = 'ИП'
        verbose_name_plural = 'ИП'

    def __str__(self):
        return "{}".format(self.iep_name)




class IndividualEntrepreneurInfo(models.Model):
    BANKS = (
        ('Альфа-банк', 'Альфа-банк'),
        ('БИНБАНК', 'БИНБАНК'),
        ('Возрождение', 'Возрождение'),
        ('Промсвязьбанк', 'Промсвязьбанк'),
        ('ВТБ', 'ВТБ'),
        ('Локо-банк', 'Локо-банк'),
        ('Модуль-банк', 'Модуль-банк'),
        ('Райффайзен-банк', 'Райффайзен-банк'),
        ('Сбербанк', 'Сбербанк'),
        ('Тинькофф', 'Тинькофф'),
        ('Точка', 'Точка'),
        ('Уралсиб', 'Уралсиб')
    )

    created_date = models.DateField(auto_now=False, auto_created=False, default=datetime.now, verbose_name='дата заполнения')
    update_date = models.DateField(auto_now_add=True, verbose_name='дата обновления')
    iep_name = models.ForeignKey('IndividualEntrepreneur', on_delete=models.CASCADE, verbose_name='ИП')
    email = models.CharField(max_length=150, blank=True, null=True, verbose_name='логин')
    password = models.CharField(max_length=100, blank=True, null=True, verbose_name='пароль')
    bank = models.CharField(max_length=100, blank=True, null=True, choices=BANKS, verbose_name='банк')
    password_of_card = models.CharField(max_length=50, null=True, blank=True, verbose_name='пароль карты')
    codeword = models.CharField(max_length=100, blank=True, null=True, verbose_name='кодовое слово')


    class Meta:
        db_table = "iep_info"
        verbose_name = "ИП инфо."
        verbose_name_plural = "ИП инфо."


class IndividualEntrepreneurSalary(models.Model):
    created_date = models.DateField(auto_now=False, auto_created=False, default=datetime.now, verbose_name='дата заполнения')
    iep = models.ForeignKey('IndividualEntrepreneur', on_delete=models.CASCADE, verbose_name='ИП')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='коментарий')
    amount = models.IntegerField(default=0, verbose_name='сумма')


    class Meta:
        db_table = "iep_salary"
        verbose_name = "ИП ЗП"
        verbose_name_plural = "ИП ЗП"


class IndividualEntrepreneurDebt(models.Model):
    created_date = models.DateField(auto_now=False, auto_created=False, default=datetime.now, verbose_name='дата заполнения')
    update_date = models.DateField(auto_now_add=True, verbose_name='дата обновления')
    iep = models.ForeignKey('IndividualEntrepreneur', on_delete=models.CASCADE, verbose_name='ИП')
    debt = models.IntegerField(default=0, verbose_name='долг')



    class Meta:
        db_table = "iep_debt"
        verbose_name = "ИП долги"
        verbose_name_plural = "ИП долги"

