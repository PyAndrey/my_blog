from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from articles.models import Post
from django.contrib.auth.models import User


def login(request):
    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            return HttpResponseRedirect(reverse('my-account', args=[user.id]))
    context = {'form': form}
    return render(request, './accounts/login2.html', context)


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


def my_account(request, id):
    # Фильтр постов по id пользователя
    posts = Post.objects.filter(owner_id=id)
    return render(request, './accounts/my_account.html', context={'posts':posts})