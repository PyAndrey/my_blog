<<<<<<< HEAD
from django.shortcuts import render

# для url без аргументов (для главной страницы)
def index(request): 
    return render(request, 'index.html')
=======
from django.http import HttpResponse

# для url без аргументов (для главной страницы)
def index(request): 
    return HttpResponse('<h1>Главная страница проекта My Blog</h1>')
>>>>>>> 7647ba4467fba21fdd20d103338fd26cecfd4f3b
