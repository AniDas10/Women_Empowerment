from django.urls import path
from . import views

urlpatterns = [
    path('fund/all/', views.womenProjects, name='women_projects'),
    path('jobs/all/', views.womenJobs, name='women_jobs'),
    path('login/', views.login, name='woman_login'),
    path('job/register/', views.jobRegister, name='woman_job_register'),
    path('fund/register/', views.fundRegister, name='woman_fund_register')
]