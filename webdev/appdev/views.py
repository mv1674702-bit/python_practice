from django.shortcuts import render, redirect
from appdev.models import Tableone

# Create your views here.

def home(request):
    if request.method == 'POST':
        name=request.POST.get('var_name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')

        # print(f"Name: {name}, Mobile: {mobile}, Email: {email}")
        Tableone.objects.create(name= name, mobile= mobile, email= email)
        return redirect("/")
    return render(request, "home.html")