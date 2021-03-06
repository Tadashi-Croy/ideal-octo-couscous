from django.urls import path
from . import views

app_name = 'pawsapp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('get_deets', views.get_deets, name='get_deets'),
    path('references/', views.references, name ='references'),
    path('contact/', views.contact, name = 'contact'),
]