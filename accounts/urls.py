<<<<<<< HEAD
from django.conf.urls import url
from django.contrib.auth.views import LoginView
=======
from django.urls import path
>>>>>>> 7647ba4467fba21fdd20d103338fd26cecfd4f3b

from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register')
]
=======
    path('sign-up', views.sign_up),
    path('sign-in', views.sign_in),
    path('my-account', views.my_account),
    path('friends/<str:user>', views.get_friends),
]
>>>>>>> 7647ba4467fba21fdd20d103338fd26cecfd4f3b
