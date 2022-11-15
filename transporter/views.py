from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from transport.forms import signUpForm
from django.contrib import messages


def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    error_message = None
    msg = "login successful"
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,msg)

                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
        else:
            error_message='Ups... something went wrong'

    context = {
        'form' : form,
        'error_message':error_message
    }
    return render(request, 'registration/login.html',context)

def signup(request):
    form = signUpForm()    
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thanks for registration')
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')


    else:
        form = signUpForm()
    context = {
        'form':form,
    }
    return render(request, 'auth/signup.html',context)

def blank_view(request):
    return render(request,'blank_page.html')