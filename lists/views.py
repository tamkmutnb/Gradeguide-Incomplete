from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Term1,Term2,Term3,Term4,Term5,Term6,Term7,Term8,GPA

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
    term2 = Term2()
    if len(Term1.objects.all()) <= 8:
        if request.POST.get('subject1Term') == "0":
            term_0 = "selected your term"
            data = Term1.objects.all()
            return render(request, 'home.html',{'term0':term_0,'list':data})
        if request.POST.get('subjectTerm') == "1":
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))

            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit'))
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8
            res = sumsub / sumunit
            if len(Term1.objects.all()) == 0 :
                Term1.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term1.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term1.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term1.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term1.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term1.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term1.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term1.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)

                GPA.objects.create(GPA_1=res)
                return render(request, 'home.html')
            else:
                Term1.objects.filter(pk=1).update(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)
                Term1.objects.filter(pk=2).update(subject =request.POST['subject2name'], unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)
                Term1.objects.filter(pk=3).update(subject =request.POST['subject3name'], unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)
                Term1.objects.filter(pk=4).update(subject =request.POST['subject4name'], unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)
                Term1.objects.filter(pk=5).update(subject =request.POST['subject5name'], unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)
                Term1.objects.filter(pk=6).update(subject =request.POST['subject6name'], unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)
                Term1.objects.filter(pk=7).update(subject =request.POST['subject7name'], unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)
                Term1.objects.filter(pk=8).update(subject =request.POST['subject8name'], unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                GPA.objects.filter(pk=1).update(GPA_1=res)

                data = Term1.objects.all()
                term1.GPA = res
                return render(request, 'home.html')

        if request.POST.get('subjectTerm') == "2":
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))

            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit'))
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8
            res = sumsub / sumunit
            if len(Term2.objects.all()) == 0 :
                Term2.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term2.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term2.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term2.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term2.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term2.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term2.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term2.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                GPA.objects.create(GPA_2=res)

                return render(request, 'home.html')
            else:
                Term2.objects.filter(pk=1).update(subject=request.POST.get('subject1name'))
                Term2.objects.filter(pk=2).update(subject=request.POST.get('subject2name'))
                Term2.objects.filter(pk=3).update(subject=request.POST.get('subject3name'))
                Term2.objects.filter(pk=4).update(subject=request.POST.get('subject4name'))
                Term2.objects.filter(pk=5).update(subject=request.POST.get('subject5name'))
                Term2.objects.filter(pk=6).update(subject=request.POST.get('subject6name'))
                Term2.objects.filter(pk=7).update(subject=request.POST.get('subject7name'))
                Term2.objects.filter(pk=8).update(subject=request.POST.get('subject8name'))
                GPA.objects.filter(pk=1).update(GPA_2=res)

                term2.GPA = res
                return render(request, 'home.html',{'result':res, 'name':request.user.username})

        if request.POST.get('subjectTerm') == "3":
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))

            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit'))
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8
            res = sumsub / sumunit
            if len(Term3.objects.all()) == 0 :
                Term3.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term3.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term3.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term3.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term3.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term3.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term3.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term3.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                GPA.objects.create(GPA_3=res)

                return render(request, 'home.html')
            else:
                Term3.objects.filter(pk=1).update(subject=request.POST.get('subject1name'))
                Term3.objects.filter(pk=2).update(subject=request.POST.get('subject2name'))
                Term3.objects.filter(pk=3).update(subject=request.POST.get('subject3name'))
                Term3.objects.filter(pk=4).update(subject=request.POST.get('subject4name'))
                Term3.objects.filter(pk=5).update(subject=request.POST.get('subject5name'))
                Term3.objects.filter(pk=6).update(subject=request.POST.get('subject6name'))
                Term3.objects.filter(pk=7).update(subject=request.POST.get('subject7name'))
                Term3.objects.filter(pk=8).update(subject=request.POST.get('subject8name'))
                GPA.objects.filter(pk=1).update(GPA_3=res)

                Term3.GPA = res
                return render(request, 'home.html')


        if request.POST.get('subjectTerm') == "4":
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))

            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit'))
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8
            res = sumsub / sumunit
            if len(Term4.objects.all()) == 0 :
                Term4.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term4.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term4.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term4.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term4.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term4.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term4.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term4.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                GPA.objects.create(GPA_4=res)

                return render(request, 'home.html')
            else:
                Term4.objects.filter(pk=1).update(subject=request.POST.get('subject1name'))
                Term4.objects.filter(pk=2).update(subject=request.POST.get('subject2name'))
                Term4.objects.filter(pk=3).update(subject=request.POST.get('subject3name'))
                Term4.objects.filter(pk=4).update(subject=request.POST.get('subject4name'))
                Term4.objects.filter(pk=5).update(subject=request.POST.get('subject5name'))
                Term4.objects.filter(pk=6).update(subject=request.POST.get('subject6name'))
                Term4.objects.filter(pk=7).update(subject=request.POST.get('subject7name'))
                Term4.objects.filter(pk=8).update(subject=request.POST.get('subject8name'))
                GPA.objects.filter(pk=1).update(GPA_4=res)

                Term4.GPA = res
                return render(request, 'home.html')
        if request.POST.get('subjectTerm') == "5":
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))

            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit'))
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8
            res = sumsub / sumunit
            if len(Term5.objects.all()) == 0 :
                Term5.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term5.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term5.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term5.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term5.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term5.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term5.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term5.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                GPA.objects.create(GPA_5=res)

                return render(request, 'home.html')
            else:
                Term5.objects.filter(pk=1).update(subject=request.POST.get('subject1name'))
                Term5.objects.filter(pk=2).update(subject=request.POST.get('subject2name'))
                Term5.objects.filter(pk=3).update(subject=request.POST.get('subject3name'))
                Term5.objects.filter(pk=4).update(subject=request.POST.get('subject4name'))
                Term5.objects.filter(pk=5).update(subject=request.POST.get('subject5name'))
                Term5.objects.filter(pk=6).update(subject=request.POST.get('subject6name'))
                Term5.objects.filter(pk=7).update(subject=request.POST.get('subject7name'))
                Term5.objects.filter(pk=8).update(subject=request.POST.get('subject8name'))
                GPA.objects.filter(pk=1).update(GPA_5=res)

                Term5.GPA = res
                return render(request, 'home.html')
        if request.POST.get('subjectTerm') == "6":
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))

            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit'))
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8
            res = sumsub / sumunit
            if len(Term6.objects.all()) == 0 :
                Term6.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term6.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term6.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term6.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term6.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term6.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term6.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term6.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                GPA.objects.create(GPA_6=res)

                return render(request, 'home.html')
            else:
                Term6.objects.filter(pk=1).update(subject=request.POST.get('subject1name'))
                Term6.objects.filter(pk=2).update(subject=request.POST.get('subject2name'))
                Term6.objects.filter(pk=3).update(subject=request.POST.get('subject3name'))
                Term6.objects.filter(pk=4).update(subject=request.POST.get('subject4name'))
                Term6.objects.filter(pk=5).update(subject=request.POST.get('subject5name'))
                Term6.objects.filter(pk=6).update(subject=request.POST.get('subject6name'))
                Term6.objects.filter(pk=7).update(subject=request.POST.get('subject7name'))
                Term6.objects.filter(pk=8).update(subject=request.POST.get('subject8name'))
                GPA.objects.filter(pk=1).update(GPA_6=res)

                Term6.GPA = res
                return render(request, 'home.html')
        if request.POST.get('subjectTerm') == "7":
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))

            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit'))
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8
            res = sumsub / sumunit
            if len(Term7.objects.all()) == 0 :
                Term7.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term7.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term7.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term7.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term7.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term7.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term7.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term7.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                GPA.objects.create(GPA_7=res)

                return render(request, 'home.html')
            else:
                Term7.objects.filter(pk=1).update(subject=request.POST.get('subject1name'))
                Term7.objects.filter(pk=2).update(subject=request.POST.get('subject2name'))
                Term7.objects.filter(pk=3).update(subject=request.POST.get('subject3name'))
                Term7.objects.filter(pk=4).update(subject=request.POST.get('subject4name'))
                Term7.objects.filter(pk=5).update(subject=request.POST.get('subject5name'))
                Term7.objects.filter(pk=6).update(subject=request.POST.get('subject6name'))
                Term7.objects.filter(pk=7).update(subject=request.POST.get('subject7name'))
                Term7.objects.filter(pk=8).update(subject=request.POST.get('subject8name'))
                GPA.objects.filter(pk=1).update(GPA_7=res)

                Term7.GPA = res
                return render(request, 'home.html')


        if request.POST.get('subjectTerm') == "8":
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))

            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit'))
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8
            res = sumsub / sumunit
            if len(Term8.objects.all()) == 0 :
                Term8.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term8.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term8.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term8.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term8.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term8.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term8.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term8.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                GPA.objects.create(GPA_8=res)

                return render(request, 'home.html')
            else:
                Term8.objects.filter(pk=1).update(subject=request.POST.get('subject1name'))
                Term8.objects.filter(pk=2).update(subject=request.POST.get('subject2name'))
                Term8.objects.filter(pk=3).update(subject=request.POST.get('subject3name'))
                Term8.objects.filter(pk=4).update(subject=request.POST.get('subject4name'))
                Term8.objects.filter(pk=5).update(subject=request.POST.get('subject5name'))
                Term8.objects.filter(pk=6).update(subject=request.POST.get('subject6name'))
                Term8.objects.filter(pk=7).update(subject=request.POST.get('subject7name'))
                Term8.objects.filter(pk=8).update(subject=request.POST.get('subject8name'))
                GPA.objects.filter(pk=1).update(GPA_8=res)

                Term8.GPA = res
                return render(request, 'home.html')
        else:
            message = "Please select term for save your grade"
            return render(request, 'home.html',{'message':message})
def termselect(request):

    termsel=str(request.POST.get('selectterm'))
    return render(request, 'home.html', {'term1': termsel})

def flow(request):
    return render(request, 'flow.html')

def Graph(request):
    dataterm_1 = Term1.objects.all()
    dataterm_2 = Term2.objects.all()
    dataGPA = GPA.objects.all()
    return render(request, 'Graph.html',{'dataterm1':dataterm_1,'dataterm2':dataterm_2,'GPARES':dataGPA})

def Result(request):
    dataterm_1 = Term1.objects.all()
    dataterm_2 = Term2.objects.all()
    dataGPA = GPA.objects.all()
    return render(request, 'Result.html',{'dataterm1':dataterm_1,'dataterm2':dataterm_2,'GPARES':dataGPA})

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