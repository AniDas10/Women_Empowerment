from django.shortcuts import render

# Create your views here.
def organisations(request):
    return render(request, 'Organisations/org_cards.html')

def organisation(request, organization_id):
    return render(request, 'Organisations/blog-single.html')