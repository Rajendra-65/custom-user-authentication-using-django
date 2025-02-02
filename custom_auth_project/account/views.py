from django.shortcuts import render
from account.forms import RegistrationForm
# Create your views here.

def register(request):
    if request.method == "POST":
        pass
    form = RegistrationForm()
    return render('/register','account/register.html',{'form':form})