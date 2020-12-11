from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, login, authenticate


def signup_view(request):
    context = {}
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        user = User.objects.create_user(
            username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
        user.save()
        login(request, user)
        print('user created')
        return redirect('home')
    else:
        return render(request, 'signup.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    else:
        context = {}
        return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
