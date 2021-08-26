from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'myproject/index.html')

def dashboard(request):
    return render(request, 'myproject/dashboard.html')

def positions(request):
    return render(request, 'myproject/positions.html')

def johnsform(request):
    return render(request, 'myproject/johnsform.html')