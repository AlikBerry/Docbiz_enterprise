# Generated by Django 2.2.8 on 2020-03-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docbiz_app', '0004_auto_20200219_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualentrepreneur',
            name='sign',
            field=models.BooleanField(default=True, verbose_name='честный знак'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='landlord',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='описание'),
        ),
    ]
