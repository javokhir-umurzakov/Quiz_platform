from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.
def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request,user)
        return redirect('/')
    return render(request,'registration/register.html',{'form':form})