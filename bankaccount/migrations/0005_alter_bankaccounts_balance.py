# Generated by Django 4.2.7 on 2023-11-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccount', '0004_alter_bankaccounts_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccounts',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]