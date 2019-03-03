from django.shortcuts import render

# Create your views here.
def womenProjects(request):
    return render(request, 'Woman/WomanNeed.html')

def womenJobs(request):
    return render(request, 'Woman/WomanJobs.html')

def login(request):
    return render(request, 'Authentication/signin.html')

def jobRegister(request):
    return render(request, 'Forms/form_job.html')

def fundRegister(request):
    return render(request, 'Forms/form_project.html')