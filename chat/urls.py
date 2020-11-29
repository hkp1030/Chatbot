from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='main'),
    path('login/', views.login, name='login'),
]