# Generated by Django 4.2.6 on 2023-12-05 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0017_alter_expense_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
    ]
