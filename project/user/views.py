from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import LoginForm, SignUpForm, UpdateForm
from .models import User

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if User.objects.filter(email=email, password=password).exists():
                messages.success(request, "Login Successful!")
                request.session['email'] = email
                return redirect('UserHome')
            else:
                messages.error(request, "Login Failed!\\nTry Again.")
                return redirect('Login')
        else:
            messages.error(request, "Login Failed!\\nTry Again.")
            return redirect('Login')
    else:
        form = LoginForm()
        return render(request, "login.html", {'form':form})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            obj = User()
            obj.username = form.cleaned_data['username']
            obj.email = form.cleaned_data['email']
            obj.password = form.cleaned_data['re_password']
            obj.address = form.cleaned_data['address']
            obj.save()
            messages.success(request, "Sign Up Successful!")
            return redirect('Home')
        else:
            messages.error(request, "Sign Up Failed!\\nTry Again.")
            return redirect('SignUp')
    else:
        form = SignUpForm()
        return render(request, "signup.html", {'form':form})

def userHome(request):
    if 'email' in request.session:
        obj = User.objects.filter()
        if not obj.exists():
            obj = None
        return render(request, "userHome.html", {'obj':obj})
    else:
        messages.error(request, "Please login first.")
        return redirect('Home')

def updateUser(request, id):
    if 'email' in request.session:
        if request.method == "POST":
            form = UpdateForm(request.POST)
            if form.is_valid():
                obj = User.objects.get(email=id)
                obj.username = form.cleaned_data['username']
                obj.email = form.cleaned_data['email']
                obj.address = form.cleaned_data['address']
                obj.save()
                messages.success(request, "User details updated successfully.")
            else:
                messages.error(request, "Failed to update user details.")
            return redirect('UserHome')
        else:
            if User.objects.filter(email=id).exists():
                obj = User.objects.filter()
                if not obj.exists():
                    obj = None
                obj1 = User.objects.get(email=id)
                print(obj1.address)
                form = UpdateForm()
                form.fields['username'].initial = obj1.username
                form.fields['email'].initial = obj1.email
                form.fields['address'].initial = obj1.address
                return render(request, "userHome.html", {'obj': obj, 'query': id, 'form':form})
            else:
                messages.error(request, "No user details found for the given email.")
                return redirect('UserHome')
    else:
        messages.error(request, "Please login first.")
        return redirect('Home')

def deleteUser(request, id):
    if 'email' in request.session:
        if User.objects.filter(email=id).exists():
            obj = User.objects.get(email=id)
            obj.delete()
            messages.success(request, "User details deleted successfully.")
        else:
            messages.error(request, "No user details found for the given email.")
        return redirect('UserHome')
    else:
        messages.error(request, "Please login first.")
        return redirect('Home')

def logout(request):
    if 'email' in request.session:
        request.session.flush()
        messages.success(request, "Logged out successfully.")
        return redirect('Home')
    else:
        messages.error(request, "Please login first.")
        return redirect('Home')