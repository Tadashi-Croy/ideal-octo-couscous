from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

app_name= 'users'

urlpatterns =[
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name= 'log_out'),
    path('personal_profile/', views.personal_profile, name='personal_profile'),
    path('personal_profile/update_dog/', views.update_dog, name='update_dog'),
    path('personal_profile/update_user/', views.update_user, name='update_user'),
    path('personal_profile/new_dog/', views.new_dog, name = 'new_dog')
]