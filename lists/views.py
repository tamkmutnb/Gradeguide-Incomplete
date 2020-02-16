from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from lists.models import Item

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
def calGrade(request):
    #cal1=int(request.POST.get('subject1Unit'))
    #cal2=int(request.POST.get('subject1Grade'))
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

    res = sumsub/sumunit
    return render(request, 'home.html',{'result':res},context)

def termselect(request):
    context={
        "Grade_term1": len(Item.objects.all())
    }
    return render(request,'home.html',context)

def flow(request):
    return render(request, 'flow.html')

def picFlow(request):
    return render(request, 'picFlow.html')