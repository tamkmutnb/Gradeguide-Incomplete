from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Term_1

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
    data = Term_1.objects.all()
    if len(data) <= 8:
        term1 = Term_1()
        term1.subject = request.POST.get('subject1name')
        term1.unit = request.POST.get('subject1Unit')
        term1.Grade = request.POST.get('subject1Grade')

        sub1 = float(request.POST.get('subject1Unit'))*float(request.POST.get('subject1Grade'))
        sub2 = float(request.POST.get('subject2Unit'))*float(request.POST.get('subject2Grade'))
        sub3 = float(request.POST.get('subject3Unit'))*float(request.POST.get('subject3Grade'))
        sub4 = float(request.POST.get('subject4Unit'))*float(request.POST.get('subject4Grade'))
        sub5 = float(request.POST.get('subject5Unit'))*float(request.POST.get('subject5Grade'))
        sub6 = float(request.POST.get('subject6Unit'))*float(request.POST.get('subject6Grade'))
        sub7 = float(request.POST.get('subject7Unit'))*float(request.POST.get('subject7Grade'))
        sub8 = float(request.POST.get('subject8Unit'))*float(request.POST.get('subject8Grade'))

        sumunit=float(request.POST.get('subject1Unit'))+float(request.POST.get('subject2Unit'))+float(request.POST.get('subject3Unit'))+float(request.POST.get('subject4Unit'))+float(request.POST.get('subject5Unit'))+float(request.POST.get('subject6Unit'))+float(request.POST.get('subject7Unit'))+float(request.POST.get('subject8Unit'))
        sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8
        res = sumsub/sumunit

        term1.GPA = res
        Term_1.objects.filter(pk=1).update(subject="New Title")
        term1.save()
        data = Term_1.objects.all()
        data1 = Term_1.objects.filter(pk=1).update(subject="New Title")
        term1.save()
        #data1 = Term_1.objects.filter(blog_id=4)
        return render(request, 'home.html',{'result':res, 'name':request.user.username,'list': data,'data123':data1})
    else:
        return render(request, 'home.html')
def termselect(request):

    termsel=str(request.POST.get('selectterm'))
    return render(request, 'home.html', {'term1': termsel})

def flow(request):
    return render(request, 'flow.html')

def picFlow(request):
    return render(request, 'picFlow.html')

def secondTerm(request):
    return render(request, 'secondTerm.html')

def thirdTerm(request):
    return render(request, 'thirdTerm.html')

def fourthTerm(request):
    return render(request, 'fourthTerm.html')

def fifthTerm(request):
    return render(request, 'fifthTerm.html')

def sixthTerm(request):
    return render(request, 'sixthTerm.html')

def seventhTerm(request):
    return render(request, 'seventhTerm.html')

def eightTerm(request):
    return render(request, 'eightTerm.html')