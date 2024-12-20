from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная страница',
        'content': 'Добро пожаловать на главную страницу!'
    }
    return render(request, 'main/index.html', context)

def onas(request):
    context = {
        'title': 'О нас',
        'content': 'Добро пожаловать на страницу "О нас"!'
    }
    return render(request, 'main/onas.html', context)

def kurs(request):
    context = {
        'title': 'Курс',
        'content': 'Добро пожаловать на страницу "Курс"!'
    }
    return render(request, 'main/kurs.html', context)

def kont(request):
    context = {
        'title': 'Контакты',
        'content': 'Добро пожаловать на страницу "Контакты"!'
    }
    return render(request, 'main/kont.html', context)
