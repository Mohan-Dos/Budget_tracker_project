from django.shortcuts import render, redirect
from .models import Expense

def index(request):
    expenses = Expense.objects.all()
    return render(request, 'index.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        title = request.POST['title']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']
        Expense.objects.create(title=title, amount=amount, category=category, date=date)
        return redirect('index')
    return render(request, 'add_expense.html')