from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # template_name='accounts/login.html' - открывает эту страницу.
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^my-account/$', views.my_account, name='my-account')
]
