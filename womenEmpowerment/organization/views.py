from django.shortcuts import render

# Create your views here.
def organisations(request):
    return render(request, 'Organisations/org_cards.html')

def organisation(request, organization_id):
    return render(request, 'Organisations/blog-single.html')

def login(request):
    return render(request, 'Authentication/signin.html')

def register(request):
    return render(request, 'Authentication/signup.html')

def adminpage(request):
    return render(request, 'Admin/index.html')

def supportform(request):
    return render(request, 'Forms/form_org.html')

def jobapp(request):
    return render(request, 'Forms/form_job.html')