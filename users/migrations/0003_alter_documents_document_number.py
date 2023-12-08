# Generated by Django 4.2.7 on 2023-12-04 09:43

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_last_confirmation_code_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='document_number',
            field=models.CharField(max_length=16, unique=True, validators=[users.models.MinLengthValidator(8)]),
        ),
    ]