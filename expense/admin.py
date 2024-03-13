from django.contrib import admin
from .models import Register, Expense
# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Age', 'Gender', 'Mobile', 'Email', 'Password')

admin.site.register(Register, RegisterAdmin)

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'Salary', 'Other_Income', 'Food', 'Transport', 'Apparel', 'Education',
                    'Grocery', 'Health', 'Other_Expense')

admin.site.register(Expense, ExpenseAdmin)
