from django.shortcuts import render
from django.http import HttpResponse

# Create your views

def home(request):
    return render(request,"home")
def about(request):
    return render(request,"about")
def contact(request):
    return render(request,"contact")

