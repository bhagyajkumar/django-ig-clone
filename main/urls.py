from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page),
    path('profile', views.profile),
    path('ajax/like-post', views.ajax_like),
]
