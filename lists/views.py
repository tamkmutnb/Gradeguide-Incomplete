from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Term1,Term2,Term3,Term4,Term5,Term6,Term7,Term8


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
    term1 = Term1()
    data1 = Term1.objects.all()
    data2 = Term2.objects.all()
    data3 = Term3.objects.all()
    data4 = Term4.objects.all()
    data5 = Term5.objects.all()
    data6 = Term6.objects.all()
    data7 = Term7.objects.all()
    data8 = Term8.objects.all()


    print(len(data1))
    if len(Term1.objects.all()) <= 8:
        if request.POST.get('subject1Term') == "0":
            term_0 = "selected your term"
            return render(request, 'home.html',{'term0':term_0})
        if request.POST.get('subject1Term') == "1":
            if len(Term1.objects.all()) == 0 :
                Term1.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'])

                Term1.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'])

                Term1.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'])


                Term1.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'])

                Term1.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'])

                Term1.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'])

                Term1.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'])
                data = Term1.objects.all()
                #1
                return render(request, 'home.html')
            else:
                Term1.objects.filter(pk=1).update(subject=request.POST.get('subject1name'))
                Term1.objects.filter(pk=2).update(subject=request.POST.get('subject2name'))
                Term1.objects.filter(pk=3).update(subject=request.POST.get('subject3name'))
                Term1.objects.filter(pk=4).update(subject=request.POST.get('subject4name'))
                Term1.objects.filter(pk=5).update(subject=request.POST.get('subject5name'))
                Term1.objects.filter(pk=6).update(subject=request.POST.get('subject6name'))
                Term1.objects.filter(pk=7).update(subject=request.POST.get('subject7name'))
                Term1.objects.filter(pk=8).update(subject=request.POST.get('subject8name'))

                #term1.subject = request.POST.get('subject1name')
               # term1.unit = request.POST.get('subject1Unit')
              # term1.Grade = request.POST.get('subject1Grade')
                #term1.subject = request.POST.get('subject2name')
               # term1.unit = request.POST.get('subject2Unit')
               # term1.Grade = request.POST.get('subject2Grade')

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

                #term1.GPA = res

                #Term1.objects.filter(pk=1).update(subject="New Title")
                #term1.save()
                #data = Term1.objects.all()
               # data789 = Term1.objects.filter(pk=110).update(subject=request.POST.get('subject1name'))
               # print(data789)
                #term1.save()
                #data1 = Term_1.objects.filter(blog_id=4)
                return render(request, 'home.html',{'result':res, 'name':request.user.username})

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