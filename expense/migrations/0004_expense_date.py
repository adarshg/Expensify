# Generated by Django 4.2.6 on 2023-11-07 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_rename_other_expense_other_expense_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='Date',
            field=models.DateField(default='1992-12-13'),
            preserve_default=False,
        ),
    ]