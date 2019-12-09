<<<<<<< HEAD
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, './accounts/register.html', context)
=======
from django.http import HttpResponse


def sign_up(request):
    return HttpResponse('<h1>Страница регистрации</h1>')


def sign_in(request):
    return HttpResponse('<h1>Страница авторизации</h1>')


def my_account(request):
    return HttpResponse('<h1>Данные вашего аккаунта</h1>')


friends = {
    'Роби Тобинсон': ['Металлий Вутко', 'Лео Месси', 'Бен Франклин', 'Твентин Карантино'],
    'Металлий Вутко': ['Металлий Вутко'],
    'Лео Месси': ['Металлий Вутко'],
    'Бен Франклин': ['Металлий Вутко', 'Лео Месси', 'Твентин Карантино', 'Elina Shake', 'Айви Яптанго'],
    'Твентин Карантино': ['Бен Франклин'],
    'Elina Shake': ['Металлий Вутко', 'Лео Месси', 'Бен Франклин'],
    'Айви Яптанго': ['Бен Франклин', 'Твентин Карантино', 'Elina Shake']
}


def get_friends(request, user):
    user_friends = friends[user]
    friends_count = len(user_friends)
    if friends_count == 1:
        return HttpResponse(f'У пользователя {user} один друг: {user_friends[0]}.')
    elif 2 <= friends_count <= 4:
        friends_string = ', '.join(user_friends)
        return HttpResponse(f'У пользователя {user} {friends_count} друга: {friends_string}.')
    elif friends_count > 4:
        friends_string = ', '.join(user_friends)
        return HttpResponse(f'У пользователя {user} {friends_count} друзей: {friends_string}.')
    else:
        return HttpResponse(f'У пользователя {user} нет друзей :(')
>>>>>>> 7647ba4467fba21fdd20d103338fd26cecfd4f3b
