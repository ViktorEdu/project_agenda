from django.urls import path, include
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]
