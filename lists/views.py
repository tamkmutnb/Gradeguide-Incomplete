from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#this is GradeGuide Page
def home_page(request):

    return render(request, 'home.html')

#this is the Real HomePage
def register(request):
    count = User.objects.count()
    return render(request, 'index.html', {
        'count': count
    })

#this is signup Page
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

#this is login page
