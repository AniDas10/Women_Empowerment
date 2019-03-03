from django.shortcuts import render

def home(request):
    return render(request, 'Main_page/index.html')

def organizations_all(request):
    return render(request, 'Main_page/organizations_all.html')