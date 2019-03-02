from django.shortcuts import render

# Create your views here.
def organisations(request):
    return render(request, 'Organisations/org_cards.html')