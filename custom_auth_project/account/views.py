from django.shortcuts import render
from account.forms import RegistrationForm
# Create your views here.

def register(request):
    if request.method == "POST":
        pass
    else:
        form = RegistrationForm()
    return render(request,'account/register.html',{'form':form})