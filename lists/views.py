from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#this is GradeGuide Page
from lists.models import Userinfo


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
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            Userinfo.objects.create(name=username)
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

#this is login page
def calGrade(request):
    #cal1=int(request.POST.get('subject1Unit'))
    #cal2=int(request.POST.get('subject1Grade'))
    user1=Userinfo.objects.get(name=request.user.username)
    user1.term1_subject_1= request.POST.get('subject1name')
    user1.term1_subject_1_unit = request.POST.get('subject1Unit')
    user1.term1_subject_1_grade = request.POST.get('subject1Grade')
    user1.save()
    test = user1.term1_subject_1
    sub1 = float(request.POST.get('subject1Unit'))*float(request.POST.get('subject1Grade'))
    sub2 = float(request.POST.get('subject2Unit'))*float(request.POST.get('subject2Grade'))
    sub3 = float(request.POST.get('subject3Unit'))*float(request.POST.get('subject3Grade'))
    sub4 = float(request.POST.get('subject4Unit'))*float(request.POST.get('subject4Grade'))
    sub5 = float(request.POST.get('subject5Unit'))*float(request.POST.get('subject5Grade'))
    sub6 = float(request.POST.get('subject6Unit'))*float(request.POST.get('subject6Grade'))
    sub7 = float(request.POST.get('subject7Unit'))*float(request.POST.get('subject7Grade'))
    sub8 = float(request.POST.get('subject8Unit'))*float(request.POST.get('subject8Grade'))#

    sumunit=float(request.POST.get('subject1Unit'))+float(request.POST.get('subject2Unit'))+float(request.POST.get('subject3Unit'))+float(request.POST.get('subject4Unit'))+float(request.POST.get('subject5Unit'))+float(request.POST.get('subject6Unit'))+float(request.POST.get('subject7Unit'))+float(request.POST.get('subject8Unit'))

    sumsub = sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8

    res = sumsub#/sumunit
    return render(request, 'home.html',{'result':res, 'name':request.user.username, 'test' : test})

def termselect(request):

    termsel=str(request.POST.get('selectterm'))
    return render(request, 'home.html', {'term1': termsel})

def flow(request):
    return render(request, 'flow.html')

def picFlow(request):
    return render(request, 'picFlow.html')