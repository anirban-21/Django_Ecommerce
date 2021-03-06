from django.shortcuts import render, redirect
from .models import Account
from .forms import RegistrationForm
from django.contrib import messages, auth
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            
            email = form.cleaned_data['email']
            username = email.split('@')[0]
            
            password = form.cleaned_data['password']
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            
            user.save()
            return redirect('login')

    else:
        form = RegistrationForm()        
    
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html',context)




def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            
            auth.login(request, user)
            return redirect('home')
                             
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')     
    return render(request, 'accounts/login.html')