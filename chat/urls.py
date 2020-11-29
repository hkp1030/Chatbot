from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='main'),
    path('', views.login, name='login'),
]