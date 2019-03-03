from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('all/', views.organisations, name='organisations'),
    path('<int:organization_id>/', views.organisation, name='organisaiton'),
    path('login/', views.login, name='organisation_login'),
    path('register/', views.register, name='organisation_register'),
    path('home/',views.homepage,name='home'),
    path('admin/',views.adminpage,name='admin'),
    path('support/',views.supportform,name='support'),
    path('job/',views.jobapp,name='job'),

]
