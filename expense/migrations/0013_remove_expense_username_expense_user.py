# Generated by Django 4.2.6 on 2023-12-04 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense', '0012_rename_user_expense_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='username',
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
