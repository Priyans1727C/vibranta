from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegisterForm

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Get the user object without saving to the database
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()  # Now save the user to the database
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('user_login')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserRegisterForm()

    return render(request, 'authentication/register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request,("there is an error occurd retry plz!"))
            return redirect('user_login')
                   
    return render(request,'authentication/login.html')


def user_logout(request):
    logout(request)
    messages.success(request,("Logout  was sucessfull"))
    return redirect(reverse('user_login'))


