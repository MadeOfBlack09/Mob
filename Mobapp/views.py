from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def HomePage(request):
    return render(request, 'Home.html')