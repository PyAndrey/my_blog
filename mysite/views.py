from django.http import HttpResponse

# для url без аргументов (для главной страницы)
def index(request): 
    return HttpResponse('<h1>Главная страница проекта My Blog</h1>')
