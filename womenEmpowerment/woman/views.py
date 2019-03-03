from django.shortcuts import render
from django.contrib.auth.models import User
from .models import WomanNeedsJob, WomanNeedsSupport
# Create your views here.
def womenProjects(request):
    return render(request, 'Woman/WomanNeed.html')

def womenJobs(request):
    return render(request, 'Woman/WomanJobs.html')

def login(request):
    return render(request, 'Authentication/signin.html')

def jobRegister(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        skills = request.POST.get('skills',None)
        about_me = request.POST.get('about_me', None)
        linkedin = request.POST.get('linkedin', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        if password2 == password:
            user = User.objects.filter(email=email)
            if user:
                print('Already exists email')
            else:
                first_name, last_name = name.split()
                woman = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
                woman.save()
                womanJob = WomanNeedsJob(about_me=about_me, skills=skills,linkedIn=linkedin, owner=woman)
                womanJob.save()
        return redirect('woman_login')
    return render(request, 'Forms/form_job.html')


def fundRegister(request):
    if request.method == 'POST':
        full_name = request.POST.get('name', None)
        project_name = request.POST.get('project_name', None)
        about_me = request.POST.get('about_me', None)
        project_description = request.POST.get('project_description', None)
        requirements = request.POST.get('requirements', None)
        photo = request.POST['profile_pic']
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        if password == password2:
            user = User.objects.filter(email=email)
            if user:
                print('Already exists')
            else:
                first_name, last_name = full_name.split()
                woman = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
                woman.save()
                womanFund = WomanNeedsSupport(project_name=project_name, about_me=about_me, project_description=project_description, requirements=requirements, photo=photo)

    return render(request, 'Forms/form_project.html')