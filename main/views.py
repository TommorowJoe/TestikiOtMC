from django.shortcuts import render, redirect
from .forms import TestForm
from .models import Test

def index(request):
    test = Test.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'test': test})


def about(request):
    return render(request, 'main/about.html')


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    else:
        form = TestForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)