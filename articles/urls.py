from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('dashboard/<int:year>', views.dashboard),
    path('<int:id>', views.article_by_id),
    path('tag/<str:tag>', views.articles_by_tag),
    path('search', views.search),
    path('add-tag', views.add_tag),
    path('check-age', views.check_age),
    path('subscribe', views.subscribe),
]