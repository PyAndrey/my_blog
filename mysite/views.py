from django.shortcuts import render

# для url без аргументов (для главной страницы)
def index(request): 
    return render(request, 'index.html')
