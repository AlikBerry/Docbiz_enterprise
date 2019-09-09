# Generated by Django 2.2 on 2019-08-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docbiz_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='contacts',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='контакты'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='type_of_activity',
            field=models.CharField(choices=[('Жора', 'Жора'), ('Хозяйственный', 'Хозяйственный'), ('Одежда', 'Одежда'), ('Продукты', 'Продукты'), ('Ресторан', 'Ресторан'), ('Сервис', 'Сервис'), ('Салон красоты', 'Салон красоты'), ('СМЦ', 'СМЦ'), ('Цветочный ряд', 'Цветочный ряд')], max_length=100, verbose_name='вид деятельности'),
        ),
    ]