from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('all/', views.organisations, name='organisations'),
    path('<int:organization_id>/', views.organisation, name='organisaiton'),
]
