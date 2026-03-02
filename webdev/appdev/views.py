from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    if request.method == 'GET':
        name=request.GET.get('var_name')
        mobile=request.GET.get('mobile')
        email=request.GET.get('email')

        print(f"Name: {name}, Mobile: {mobile}, Email: {email}")
    return render(request, 'home.html')