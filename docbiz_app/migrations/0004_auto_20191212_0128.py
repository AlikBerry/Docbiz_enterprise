# Generated by Django 2.2.8 on 2019-12-11 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docbiz_app', '0003_auto_20191003_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='type_of_activity',
            field=models.CharField(blank=True, choices=[('Жора', 'Жора'), ('Интернет-магазин', 'Интернет-магазин'), ('Стройматреиалы', 'Стройматериалы'), ('Хозяйственный', 'Хозяйственный'), ('Магазин', 'Магазин'), ('Одежда', 'Одежда'), ('Продукты', 'Продукты'), ('Ресторан', 'Ресторан'), ('Сервис', 'Сервис'), ('Салон красоты', 'Салон красоты'), ('СМЦ', 'СМЦ'), ('Цветочный ряд', 'Цветочный ряд')], max_length=50, null=True, verbose_name='вид деятельности'),
        ),
        migrations.AlterField(
            model_name='individualentrepreneurinfo',
            name='bank',
            field=models.CharField(blank=True, choices=[('Альфа-банк', 'Альфа-банк'), ('БИНБАНК', 'БИНБАНК'), ('Возрождение', 'Возрождение'), ('Промсвязьбанк', 'Промсвязьбанк'), ('ВТБ', 'ВТБ'), ('Локо-банк', 'Локо-банк'), ('Модуль-банк', 'Модуль-банк'), ('Райффайзен-банк', 'Райффайзен-банк'), ('Сбербанк', 'Сбербанк'), ('Тинькофф', 'Тинькофф'), ('Точка', 'Точка'), ('Уралсиб', 'Уралсиб')], max_length=100, null=True, verbose_name='банк'),
        ),
    ]