from django.shortcuts import render
from .models import Account
from .forms import RegistrationForm
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

    else:
        form = RegistrationForm()        
    
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html',context)