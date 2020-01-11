from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # template_name='accounts/login.html' - открывает эту страницу.
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('<int:id>/', views.my_account, name='my-account')
]
