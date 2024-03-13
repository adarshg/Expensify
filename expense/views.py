from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Register, Expense
from .forms import CreateUserForm, ExpenseForm
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'home.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully")
            return redirect('login')
    context = {
            'form': form
    }
    return render(request, 'register.html', context)

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/expensepage/')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'login.html')

def expensecalc(request):
    try:
        expens = Expense.objects.filter(user=request.user)
        sum1 = expens.aggregate(total_sum=Sum('Salary'))
        inc_sum1 = sum1['total_sum']
        sum2 = expens.aggregate(total_sum=Sum('Other_Income'))
        inc_sum2 = sum2['total_sum']
        total_inc = inc_sum1 + inc_sum2
        sum3 = expens.aggregate(total_sum=Sum('Food'))
        exp_sum1 = sum3['total_sum']
        sum4 = expens.aggregate(total_sum=Sum('Transport'))
        exp_sum2 = sum4['total_sum']
        sum5 = expens.aggregate(total_sum=Sum('Apparel'))
        exp_sum3 = sum5['total_sum']
        sum4 = expens.aggregate(total_sum=Sum('Education'))
        exp_sum4 = sum4['total_sum']
        sum5 = expens.aggregate(total_sum=Sum('Grocery'))
        exp_sum5 = sum5['total_sum']
        sum6 = expens.aggregate(total_sum=Sum('Health'))
        exp_sum6 = sum6['total_sum']
        sum7 = expens.aggregate(total_sum=Sum('Other_Expense'))
        exp_sum7 = sum7['total_sum']
        total_exp = exp_sum1 + exp_sum2 + exp_sum3 + exp_sum4 + exp_sum5 + exp_sum6 + exp_sum7
        total = total_inc - total_exp
    except Exception as e:
        expens = None
        total_inc = 0
        total_exp = 0
        total = 0
    exp = {
        'expens': expens,
        'total_inc': total_inc,
        'total_exp': total_exp,
        'total': total
    }
    return render(request, 'expenses.html', exp)

def addExpense(request):
    default = {
        'user': request.user,
        'Salary': 0,
        'Other_Income': 0,
        'Food': 0,
        'Transport': 0,
        'Apparel': 0,
        'Education': 0,
        'Grocery': 0,
        'Health': 0,
        'Other_Expense': 0

    }
    form = ExpenseForm(request.POST or None, initial=default)
    if form.is_valid():
        # expense = form.save(commit=False)
        # expense.user = request.user
        # expense.save()
        form.save()
        return redirect('/expensepage/')
    else:
        print(form.errors)
    return render(request, 'add_expense.html', {'form': form})

def filterExpense(request):
    # expenseForm = Expense.objects.all()
    if request.method == 'POST':
        fromdate = request.POST.get('from_date')
        todate = request.POST.get('to_date')
        # if fromdate:
        try:
            expenseForm = Expense.objects.filter(Date__gte=fromdate, Date__lte=todate, user=request.user)

            # if todate:
            #     expenseForm = expenseForm.filter(Date__lte=todate)
            sum1 = expenseForm.aggregate(total_sum=Sum('Salary'))
            inc_sum1 = sum1['total_sum']
            sum2 = expenseForm.aggregate(total_sum=Sum('Other_Income'))
            inc_sum2 = sum2['total_sum']
            total_inc = inc_sum1 + inc_sum2
            sum3 = expenseForm.aggregate(total_sum=Sum('Food'))
            exp_sum1 = sum3['total_sum']
            sum4 = expenseForm.aggregate(total_sum=Sum('Transport'))
            exp_sum2 = sum4['total_sum']
            sum5 = expenseForm.aggregate(total_sum=Sum('Apparel'))
            exp_sum3 = sum5['total_sum']
            sum4 = expenseForm.aggregate(total_sum=Sum('Education'))
            exp_sum4 = sum4['total_sum']
            sum5 = expenseForm.aggregate(total_sum=Sum('Grocery'))
            exp_sum5 = sum5['total_sum']
            sum6 = expenseForm.aggregate(total_sum=Sum('Health'))
            exp_sum6 = sum6['total_sum']
            sum7 = expenseForm.aggregate(total_sum=Sum('Other_Expense'))
            exp_sum7 = sum7['total_sum']
            total_exp = exp_sum1 + exp_sum2 + exp_sum3 + exp_sum4 + exp_sum5 + exp_sum6 + exp_sum7
            total = total_inc - total_exp
        except:
            expenseForm = None
            total_inc = 0
            total_exp = 0
            total = 0
            messages.info(request, 'No data found in the dates specified')

        context = {'expenseForm': expenseForm,
                    'total_inc': total_inc,
                   'total_exp': total_exp,
                   'total': total
        }
        return render(request, 'filter_expense.html', context)
    return render(request, 'filter_expense.html')
