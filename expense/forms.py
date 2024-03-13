from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Expense

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DateInput(forms.DateInput):
    input_type = 'date'

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        # fields = ['Date', 'Salary', 'Other_Income', 'Food', 'Transport', 'Apparel',
        #           'Education', 'Grocery', 'Health', 'Other_Expense']
        # exclude = ['user']

        widgets = {
            'Date': DateInput()
        }
