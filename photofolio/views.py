from django.shortcuts import render

# Create your views here.
def photofolio(request):
    return render(request, 'photofolio.html')
