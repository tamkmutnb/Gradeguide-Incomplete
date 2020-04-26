from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Term1, Term2, Term3, Term4, Term5, Term6, Term7, Term8, GPA

# this is GradeGuide Page
from lists.models import Userinfo


def home_page(request):
    # return home.html
    return render(request, 'home.html')


# this is the Real HomePage
def register(request):
    # create dataGPA var to collect GPA objects
    dataGPA = GPA.objects.all()
    # if dataGPA is empty create one containing(8 gpas)
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    # count registered user
    # and show on index page
    count = User.objects.count()
    return render(request, 'index.html', {
        'count': count
    })


# this is signup Page
def signup(request):
    # use django signup form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # if form is correct create new user
        # save all user data and auto login
        # else return to signup page
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


# this is login page
def calGrade(request):
    term1 = Term1()
    term2 = Term2()
    # warning text if user doesn't input info correctly
    not_input = "Plese check your infromation before saving."
    # checkinput by addding all unit and grade
    checkinput = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject1Grade')) + \
                 float(request.POST.get('subject2Unit')) + float(request.POST.get('subject2Grade')) + \
                 float(request.POST.get('subject3Unit')) + float(request.POST.get('subject3Grade')) + \
                 float(request.POST.get('subject4Unit')) + float(request.POST.get('subject4Grade')) + \
                 float(request.POST.get('subject5Unit')) + float(request.POST.get('subject5Grade')) + \
                 float(request.POST.get('subject6Unit')) + float(request.POST.get('subject6Grade')) + \
                 float(request.POST.get('subject7Unit')) + float(request.POST.get('subject7Grade')) + \
                 float(request.POST.get('subject8Unit')) + float(request.POST.get('subject8Grade')) + \
                 float(request.POST.get('subject9Unit')) + float(request.POST.get('subject9Grade'))
    # if term object is less than equal 9
    if len(Term1.objects.all()) <= 9:
        # check if request is correct term
        if request.POST.get('subjectTerm') == "1":
            # if checkinput = 0 return home.html
            if checkinput == 0.0:
                return render(request, 'home.html', {'notinput': not_input})
            # calculate each sub by (unit*grade)
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            # sum all subjects unit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )
            # sum all sub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # calculating GPA
            res = sumsub / sumunit
            # if term objects is empty
            # create new one for each subject containing (subjectname, unit, grade and GPA)
            if len(Term1.objects.all()) == 0:
                Term1.objects.create(subject=request.POST['subject1name'], unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'], GPA=res)

                Term1.objects.create(subject=request.POST['subject2name'], unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'], GPA=res)

                Term1.objects.create(subject=request.POST['subject3name'], unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'], GPA=res)

                Term1.objects.create(subject=request.POST['subject4name'], unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'], GPA=res)

                Term1.objects.create(subject=request.POST['subject5name'], unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'], GPA=res)

                Term1.objects.create(subject=request.POST['subject6name'], unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'], GPA=res)

                Term1.objects.create(subject=request.POST['subject7name'], unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'], GPA=res)

                Term1.objects.create(subject=request.POST['subject8name'], unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'], GPA=res)

                Term1.objects.create(subject=request.POST['subject9name'], unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'], GPA=res)
                GPA.objects.filter(pk=1).update(GPA_1=res)

                # reuturn GPA to home.html page
                return render(request, 'home.html', {'result': res})
            # else update one for each subject containing (subjectname, unit, grade and GPA)
            else:
                Term1.objects.filter(pk=1).update(subject=request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'],
                                                  Grade=request.POST['subject1Grade'], GPA=res)
                Term1.objects.filter(pk=2).update(subject=request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'], GPA=res)
                Term1.objects.filter(pk=3).update(subject=request.POST['subject3name'],
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'], GPA=res)
                Term1.objects.filter(pk=4).update(subject=request.POST['subject4name'],
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'], GPA=res)
                Term1.objects.filter(pk=5).update(subject=request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'], GPA=res)
                Term1.objects.filter(pk=6).update(subject=request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'], GPA=res)
                Term1.objects.filter(pk=7).update(subject=request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'], GPA=res)
                Term1.objects.filter(pk=8).update(subject=request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'], GPA=res)
                Term1.objects.filter(pk=9).update(subject=request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'], GPA=res)

                GPA.objects.filter(pk=1).update(GPA_1=res)

                data = Term1.objects.all()
                term1.GPA = res
                return render(request, 'home.html', {'result': res})
        # check if request is correct term
        if request.POST.get('subjectTerm') == "2":
            # if checkinput = 0 return home.html
            if checkinput == 0.0:
                return render(request, 'home.html', {'notinput': not_input})
            # calculate each sub by (unit*grade)
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            # sum all subjects unit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )
            # sum all sub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # calculating GPA
            res = sumsub / sumunit
            # if term objects is empty
            # create new one for each subject containing (subjectname, unit, grade and GPA)
            if len(Term2.objects.all()) == 0:
                Term2.objects.create(subject=request.POST['subject1name'], unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'], GPA=res)

                Term2.objects.create(subject=request.POST['subject2name'], unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'], GPA=res)

                Term2.objects.create(subject=request.POST['subject3name'], unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'], GPA=res)

                Term2.objects.create(subject=request.POST['subject4name'], unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'], GPA=res)

                Term2.objects.create(subject=request.POST['subject5name'], unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'], GPA=res)

                Term2.objects.create(subject=request.POST['subject6name'], unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'], GPA=res)

                Term2.objects.create(subject=request.POST['subject7name'], unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'], GPA=res)

                Term2.objects.create(subject=request.POST['subject8name'], unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'], GPA=res)

                Term2.objects.create(subject=request.POST['subject9name'], unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'], GPA=res)
                GPA.objects.filter(pk=1).update(GPA_2=res)
                # reuturn GPA to home.html page
                return render(request, 'home.html', {'result': res})
            # else update one for each subject containing (subjectname, unit, grade and GPA)
            else:
                Term2.objects.filter(pk=1).update(subject=request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'],
                                                  Grade=request.POST['subject1Grade'], GPA=res)
                Term2.objects.filter(pk=2).update(subject=request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'], GPA=res)
                Term2.objects.filter(pk=3).update(subject=request.POST['subject3name'],
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'], GPA=res)
                Term2.objects.filter(pk=4).update(subject=request.POST['subject4name'],
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'], GPA=res)
                Term2.objects.filter(pk=5).update(subject=request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'], GPA=res)
                Term2.objects.filter(pk=6).update(subject=request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'], GPA=res)
                Term2.objects.filter(pk=7).update(subject=request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'], GPA=res)
                Term2.objects.filter(pk=8).update(subject=request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'], GPA=res)
                Term2.objects.filter(pk=9).update(subject=request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'], GPA=res)

                GPA.objects.filter(pk=1).update(GPA_2=res)

                term2.GPA = res
                return render(request, 'home.html', {'result': res})

        if request.POST.get('subjectTerm') == "3":
            # if checkinput = 0 return home.html
            if checkinput == 0.0:
                return render(request, 'home.html', {'notinput': not_input})
            # calculate each sub by (unit*grade)
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            # sum all subjects unit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )
            # sum all sub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # calculating GPA
            res = sumsub / sumunit
            # if term objects is empty
            # create new one for each subject containing (subjectname, unit, grade and GPA)
            if len(Term3.objects.all()) == 0:
                Term3.objects.create(subject=request.POST['subject1name'], unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'], GPA=res)

                Term3.objects.create(subject=request.POST['subject2name'], unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'], GPA=res)

                Term3.objects.create(subject=request.POST['subject3name'], unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'], GPA=res)

                Term3.objects.create(subject=request.POST['subject4name'], unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'], GPA=res)

                Term3.objects.create(subject=request.POST['subject5name'], unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'], GPA=res)

                Term3.objects.create(subject=request.POST['subject6name'], unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'], GPA=res)

                Term3.objects.create(subject=request.POST['subject7name'], unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'], GPA=res)

                Term3.objects.create(subject=request.POST['subject8name'], unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'], GPA=res)

                Term3.objects.create(subject=request.POST['subject9name'], unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'], GPA=res)
                GPA.objects.filter(pk=1).update(GPA_3=res)

                # reuturn GPA to home.html page

                return render(request, 'home.html', {'result': res})
            # else update one for each subject containing (subjectname, unit, grade and GPA)
            else:
                Term3.objects.filter(pk=1).update(subject=request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'],
                                                  Grade=request.POST['subject1Grade'], GPA=res)
                Term3.objects.filter(pk=2).update(subject=request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'], GPA=res)
                Term3.objects.filter(pk=3).update(subject=request.POST['subject3name'],
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'], GPA=res)
                Term3.objects.filter(pk=4).update(subject=request.POST['subject4name'],
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'], GPA=res)
                Term3.objects.filter(pk=5).update(subject=request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'], GPA=res)
                Term3.objects.filter(pk=6).update(subject=request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'], GPA=res)
                Term3.objects.filter(pk=7).update(subject=request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'], GPA=res)
                Term3.objects.filter(pk=8).update(subject=request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'], GPA=res)
                Term3.objects.filter(pk=9).update(subject=request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'], GPA=res)
                GPA.objects.filter(pk=1).update(GPA_3=res)

                Term3.GPA = res
                return render(request, 'home.html', {'result': res})

        if request.POST.get('subjectTerm') == "4":
            # if checkinput = 0 return home.html
            if checkinput == 0.0:
                return render(request, 'home.html', {'notinput': not_input})
            # calculate each sub by (unit*grade)
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            # sum all subjects unit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )
            # sum all sub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # calculating GPA
            res = sumsub / sumunit
            # if term objects is empty
            # create new one for each subject containing (subjectname, unit, grade and GPA)
            if len(Term4.objects.all()) == 0:
                Term4.objects.create(subject=request.POST['subject1name'], unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'], GPA=res)

                Term4.objects.create(subject=request.POST['subject2name'], unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'], GPA=res)

                Term4.objects.create(subject=request.POST['subject3name'], unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'], GPA=res)

                Term4.objects.create(subject=request.POST['subject4name'], unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'], GPA=res)

                Term4.objects.create(subject=request.POST['subject5name'], unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'], GPA=res)

                Term4.objects.create(subject=request.POST['subject6name'], unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'], GPA=res)

                Term4.objects.create(subject=request.POST['subject7name'], unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'], GPA=res)

                Term4.objects.create(subject=request.POST['subject8name'], unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'], GPA=res)

                Term4.objects.create(subject=request.POST['subject9name'], unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'], GPA=res)
                GPA.objects.filter(pk=1).update(GPA_4=res)
                # reuturn GPA to home.html page
                return render(request, 'home.html', {'result': res})
            # else update one for each subject containing (subjectname, unit, grade and GPA)
            else:
                Term4.objects.filter(pk=1).update(subject=request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'],
                                                  Grade=request.POST['subject1Grade'], GPA=res)
                Term4.objects.filter(pk=2).update(subject=request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'], GPA=res)
                Term4.objects.filter(pk=3).update(subject=request.POST['subject3name'],
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'], GPA=res)
                Term4.objects.filter(pk=4).update(subject=request.POST['subject4name'],
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'], GPA=res)
                Term4.objects.filter(pk=5).update(subject=request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'], GPA=res)
                Term4.objects.filter(pk=6).update(subject=request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'], GPA=res)
                Term4.objects.filter(pk=7).update(subject=request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'], GPA=res)
                Term4.objects.filter(pk=8).update(subject=request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'], GPA=res)
                Term4.objects.filter(pk=9).update(subject=request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'], GPA=res)
                GPA.objects.filter(pk=1).update(GPA_4=res)

                Term4.GPA = res
                return render(request, 'home.html', {'result': res})
        if request.POST.get('subjectTerm') == "5":
            # if checkinput = 0 return home.html
            if checkinput == 0.0:
                return render(request, 'home.html', {'notinput': not_input})
            # calculate each sub by (unit*grade)
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))
            # sum all subjects unit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )
            # sum all sub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # calculating GPA
            res = sumsub / sumunit
            # if term objects is empty
            # create new one for each subject containing (subjectname, unit, grade and GPA)
            if len(Term5.objects.all()) == 0:
                Term5.objects.create(subject=request.POST['subject1name'], unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'], GPA=res)

                Term5.objects.create(subject=request.POST['subject2name'], unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'], GPA=res)

                Term5.objects.create(subject=request.POST['subject3name'], unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'], GPA=res)

                Term5.objects.create(subject=request.POST['subject4name'], unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'], GPA=res)

                Term5.objects.create(subject=request.POST['subject5name'], unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'], GPA=res)

                Term5.objects.create(subject=request.POST['subject6name'], unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'], GPA=res)

                Term5.objects.create(subject=request.POST['subject7name'], unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'], GPA=res)

                Term5.objects.create(subject=request.POST['subject8name'], unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'], GPA=res)

                Term5.objects.create(subject=request.POST['subject9name'], unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'], GPA=res)
                # reuturn GPA to home.html page
                GPA.objects.filter(pk=1).update(GPA_5=res)

                return render(request, 'home.html', {'result': res})
            # else update one for each subject containing (subjectname, unit, grade and GPA)
            else:
                Term5.objects.filter(pk=1).update(subject=request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'],
                                                  Grade=request.POST['subject1Grade'], GPA=res)
                Term5.objects.filter(pk=2).update(subject=request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'], GPA=res)
                Term5.objects.filter(pk=3).update(subject=request.POST['subject3name'],
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'], GPA=res)
                Term5.objects.filter(pk=4).update(subject=request.POST['subject4name'],
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'], GPA=res)
                Term5.objects.filter(pk=5).update(subject=request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'], GPA=res)
                Term5.objects.filter(pk=6).update(subject=request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'], GPA=res)
                Term5.objects.filter(pk=7).update(subject=request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'], GPA=res)
                Term5.objects.filter(pk=8).update(subject=request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'], GPA=res)
                Term5.objects.filter(pk=9).update(subject=request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'], GPA=res)
                GPA.objects.filter(pk=1).update(GPA_5=res)

                Term5.GPA = res
                return render(request, 'home.html', {'result': res})
        if request.POST.get('subjectTerm') == "6":
            # if checkinput = 0 return home.html
            if checkinput == 0.0:
                return render(request, 'home.html', {'notinput': not_input})
            # calculate each sub by (unit*grade)
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))
            # sum all subjects unit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )
            # sum all sub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # calculating GPA
            res = sumsub / sumunit
            # if term objects is empty
            # create new one for each subject containing (subjectname, unit, grade and GPA)
            if len(Term6.objects.all()) == 0:
                Term6.objects.create(subject=request.POST['subject1name'], unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'], GPA=res)

                Term6.objects.create(subject=request.POST['subject2name'], unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'], GPA=res)

                Term6.objects.create(subject=request.POST['subject3name'], unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'], GPA=res)

                Term6.objects.create(subject=request.POST['subject4name'], unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'], GPA=res)

                Term6.objects.create(subject=request.POST['subject5name'], unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'], GPA=res)

                Term6.objects.create(subject=request.POST['subject6name'], unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'], GPA=res)

                Term6.objects.create(subject=request.POST['subject7name'], unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'], GPA=res)

                Term6.objects.create(subject=request.POST['subject8name'], unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'], GPA=res)

                Term6.objects.create(subject=request.POST['subject9name'], unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'], GPA=res)
                GPA.objects.filter(pk=1).update(GPA_6=res)
                # reuturn GPA to home.html page
                return render(request, 'home.html', {'result': res})
            # else update one for each subject containing (subjectname, unit, grade and GPA)
            else:
                Term6.objects.filter(pk=1).update(subject=request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'],
                                                  Grade=request.POST['subject1Grade'], GPA=res)
                Term6.objects.filter(pk=2).update(subject=request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'], GPA=res)
                Term6.objects.filter(pk=3).update(subject=request.POST['subject3name'],
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'], GPA=res)
                Term6.objects.filter(pk=4).update(subject=request.POST['subject4name'],
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'], GPA=res)
                Term6.objects.filter(pk=5).update(subject=request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'], GPA=res)
                Term6.objects.filter(pk=6).update(subject=request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'], GPA=res)
                Term6.objects.filter(pk=7).update(subject=request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'], GPA=res)
                Term6.objects.filter(pk=8).update(subject=request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'], GPA=res)
                Term6.objects.filter(pk=9).update(subject=request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'], GPA=res)
                GPA.objects.filter(pk=1).update(GPA_6=res)

                Term6.GPA = res
                return render(request, 'home.html', {'result': res})
        if request.POST.get('subjectTerm') == "7":
            # if checkinput = 0 return home.html
            if checkinput == 0.0:
                return render(request, 'home.html', {'notinput': not_input})
            # calculate each sub by (unit*grade)
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))
            # sum all subjects unit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )
            # sum all sub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # calculating GPA
            res = sumsub / sumunit
            # if term objects is empty
            # create new one for each subject containing (subjectname, unit, grade and GPA)
            if len(Term7.objects.all()) == 0:
                Term7.objects.create(subject=request.POST['subject1name'], unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'], GPA=res)

                Term7.objects.create(subject=request.POST['subject2name'], unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'], GPA=res)

                Term7.objects.create(subject=request.POST['subject3name'], unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'], GPA=res)

                Term7.objects.create(subject=request.POST['subject4name'], unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'], GPA=res)

                Term7.objects.create(subject=request.POST['subject5name'], unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'], GPA=res)

                Term7.objects.create(subject=request.POST['subject6name'], unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'], GPA=res)

                Term7.objects.create(subject=request.POST['subject7name'], unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'], GPA=res)

                Term7.objects.create(subject=request.POST['subject8name'], unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'], GPA=res)

                Term7.objects.create(subject=request.POST['subject9name'], unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'], GPA=res)
                # reuturn GPA to home.html page
                GPA.objects.filter(pk=1).update(GPA_7=res)

                return render(request, 'home.html', {'result': res})
            # else update one for each subject containing (subjectname, unit, grade and GPA)
            else:
                Term6.objects.filter(pk=1).update(subject=request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'],
                                                  Grade=request.POST['subject1Grade'], GPA=res)
                Term6.objects.filter(pk=2).update(subject=request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'], GPA=res)
                Term6.objects.filter(pk=3).update(subject=request.POST['subject3name'],
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'], GPA=res)
                Term6.objects.filter(pk=4).update(subject=request.POST['subject4name'],
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'], GPA=res)
                Term6.objects.filter(pk=5).update(subject=request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'], GPA=res)
                Term6.objects.filter(pk=6).update(subject=request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'], GPA=res)
                Term6.objects.filter(pk=7).update(subject=request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'], GPA=res)
                Term6.objects.filter(pk=8).update(subject=request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'], GPA=res)
                Term6.objects.filter(pk=9).update(subject=request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'], GPA=res)
                GPA.objects.filter(pk=1).update(GPA_7=res)

                Term7.GPA = res
                return render(request, 'home.html', {'result': res})

        if request.POST.get('subjectTerm') == "8":
            # if checkinput = 0 return home.html
            if checkinput == 0.0:
                return render(request, 'home.html', {'notinput': not_input})
            # calculate each sub by (unit*grade)
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))
            # sum all subjects unit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )
            # sum all sub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # calculating GPA
            res = sumsub / sumunit
            # if term objects is empty
            # create new one for each subject containing (subjectname, unit, grade and GPA)
            if len(Term8.objects.all()) == 0:
                Term8.objects.create(subject=request.POST['subject1name'], unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'], GPA=res)

                Term8.objects.create(subject=request.POST['subject2name'], unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'], GPA=res)

                Term8.objects.create(subject=request.POST['subject3name'], unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'], GPA=res)

                Term8.objects.create(subject=request.POST['subject4name'], unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'], GPA=res)

                Term8.objects.create(subject=request.POST['subject5name'], unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'], GPA=res)

                Term8.objects.create(subject=request.POST['subject6name'], unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'], GPA=res)

                Term8.objects.create(subject=request.POST['subject7name'], unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'], GPA=res)

                Term8.objects.create(subject=request.POST['subject8name'], unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'], GPA=res)

                Term8.objects.create(subject=request.POST['subject9name'], unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'], GPA=res)
                GPA.objects.filter(pk=1).update(GPA_8=res)
                # reuturn GPA to home.html page
                return render(request, 'home.html', {'result': res})
            # else update one for each subject containing (subjectname, unit, grade and GPA)
            else:
                Term6.objects.filter(pk=1).update(subject=request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'],
                                                  Grade=request.POST['subject1Grade'], GPA=res)
                Term6.objects.filter(pk=2).update(subject=request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'], GPA=res)
                Term6.objects.filter(pk=3).update(subject=request.POST['subject3name'],
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'], GPA=res)
                Term6.objects.filter(pk=4).update(subject=request.POST['subject4name'],
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'], GPA=res)
                Term6.objects.filter(pk=5).update(subject=request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'], GPA=res)
                Term6.objects.filter(pk=6).update(subject=request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'], GPA=res)
                Term6.objects.filter(pk=7).update(subject=request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'], GPA=res)
                Term6.objects.filter(pk=8).update(subject=request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'], GPA=res)
                Term6.objects.filter(pk=9).update(subject=request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'], GPA=res)
                GPA.objects.filter(pk=1).update(GPA_8=res)

                Term8.GPA = res
                return render(request, 'home.html', {'result': res})
        else:
            message = 'Please select term before saving grade'
            return render(request, 'home.html', {'message': message})


def termselect(request):
    # collect selected term user use
    termsel = str(request.POST.get('selectterm'))
    # return home.html with term selected
    return render(request, 'home.html', {'term1': termsel})


def flow(request):
    Result = ''
    subjects = str(request.POST.get('searchFlow', ''))
    if 'searchSubject' in request.POST:
        # 1ProFund
        if subjects == "Programming Fundamental":
            Result = """Semister2 : Algorithms and Data Structures <br />
            Semister5 : Operating Systems"""
        # 2MathI
        elif subjects == "Engineering Mathematics I":
            Result = """Semister2 : Math II <br />
            Semister3 : Statistics for Computer Engineer"""
        # 3ComExplo
        elif subjects == "Computer Engineering Exploration":
            Result = "The subject hasn't other subjects to connect the flow"
        # 4PhysicsI
        elif subjects == "Physics I":
            Result = "Semister2 : Physics II"
        # 5PhyLabI
        elif subjects == "Physics Laboratory I":
            Result = "The subject hasn't other subjects to connect the flow"
        # 6EnglishI
        elif subjects == "Language Elective Course I":
            Result = "Language Elective Course II"
        # 7TableTennis
        elif subjects == "Physical Education Elective Course I":
            Result = "Physical Education Elective Course II"
        # 8ManSo
        elif subjects == "Social Sciences Elective Course":
            Result = "The subject hasn't other subjects to connect the flow"
        # 9Intro
        elif subjects == "Introduction to Engineer":
            Result = "The subject hasn't other subjects to connect the flow"
        # 10Circuit
        elif subjects == "Electric Circuit Theory":
            Result = "Semister4 : Analog and Digital Electronics"
        # 11CircuitLab
        elif subjects == "Electric Circuit Lab":
            Result = "The subject hasn't other subjects to connect the flow"
        # 12Algo
        elif subjects == "Algorithms and Data Structure":
            Result = """Semister3 : Software Development Practice I <br />
            Semister5 : Computer Organization <br />
            Semister6 : Database Systems"""
        # 13Work Ethics
        elif subjects == "Work Ethics":
            Result = "The subject hasn't other subjects to connect the flow"
        # 14MathII
        elif subjects == "Engineering Mathematics II":
            Result = """Semister3 : Discrete Mathematics <br />
            Semister3 : Introduction to Signals and System"""
        # 15PhysicsII
        elif subjects == "Physics II":
            Result = "The subject hasn't other subjects to connect the flow"
        # 16PhyLab2
        elif subjects == "Physics Laboratory II":
            Result = "The subject hasn't other subjects to connect the flow"
        # 17EnglishII
        elif subjects == "Language Elective Course II":
            Result = "Language Elective Course III"
        # 18Basketball
        elif subjects == "Physical Education Elective Course II":
            Result = "The subject hasn't other subjects to connect the flow"
        # 19Stat
        elif subjects == "Statistics for Computer Engineer":
            Result = "The subject hasn't other subjects to connect the flow"
        # 20Signal
        elif subjects == "Introduction to Signals and System":
            Result = "The subject hasn't other subjects to connect the flow"
        # 21Digital
        elif subjects == "Logic Design of Digital System":
            Result = """Semister3 : Digital System Design Laboratory <br />
            Semister4 : Computer Organization"""
        # 22DigiLab
        elif subjects == "Digital System Design Laboratory":
            Result = "The subject hasn't other subjects to connect the flow"
        # 23SoftwareI
        elif subjects == "Software Development Practice I":
            Result = "Semister4 : Software Development Practice II"
        # 24Discrete Math
        elif subjects == "Discrete Mathematics":
            Result = "Semister6 : Database Systems"
        # 25PhyLife
        elif subjects == "Science and Maths Elective I":
            Result = "Science and Maths Elective II"
        # 26SoftwareII
        elif subjects == "Software Development Practice II":
            Result = "Semister5 : Software Engineering"
        # 27NetworkI
        elif subjects == "Computer Networks I":
            Result = "Semister5 : Computer Networks II"
        # 28ComOr
        elif subjects == "Computer Organization":
            Result = "Semister5 : Embedded System Design"
        # 29Ubi
        elif subjects == "Ubiquitous Computing":
            Result = "The subject hasn't other subjects to connect the flow"
        # 30Analog
        elif subjects == "Analog and Digital Electronics":
            Result = "Semister5 : Analog and Digital Electronics Lab"
        # 31GenMath
        elif subjects == "Science and Maths Elective II":
            Result = "Science and Maths Elective III"
        # 32SoftEng
        elif subjects == "Software Engineering":
            Result = "The subject hasn't other subjects to connect the flow"
        # 33NetworkII
        elif subjects == "Computer Networks II":
            Result = "Semister6 : Computer Networks Lab"
        # 34OS
        elif subjects == "Operating Systems":
            Result = "The subject hasn't other subjects to connect the flow"
        # 35Embedded
        elif subjects == "Embedded System Design":
            Result = "Semister6 : Embedded System Design Laboratory"
        # 36AnalogLab
        elif subjects == "Analog and Digital Electronics Lab":
            Result = "The subject hasn't other subjects to connect the flow"
        # 37Language Elective III
        elif subjects == "Language Elective Course III":
            Result = "Language Elective Course IV"
        # 38Database
        elif subjects == "Database Systems":
            Result = "The subject hasn't other subjects to connect the flow"
        # 39NetworkLab
        elif subjects == "Computer Networks Lab":
            Result = "The subject hasn't other subjects to connect the flow"
        # 40EmbeddedLab
        elif subjects == "Embedded System Design Laboratory":
            Result = "The subject hasn't other subjects to connect the flow"
        # 41Language Elective IV
        elif subjects == "Language Elective Course IV":
            Result = "The subject hasn't other subjects to connect the flow"
        # 42Computer Eng. Elective Course I
        elif subjects == "Computer Eng. Elective Course I":
            Result = "Computer Eng. Elective Course II"
        # 43Computer Eng. Elective Course II
        elif subjects == "Computer Eng. Elective Course II":
            Result = "The subject hasn't other subjects to connect the flow"
        # 44Humanities Elective Course I
        elif subjects == "Humanities Elective Course I":
            Result = "Humanities Elective Course II"
        # 45ProjectI
        elif subjects == "Project I":
            Result = "Semister8 : Project II"
        # 46Free Elective Course I
        elif subjects == "Free Elective Course I":
            Result = "Free Elective Course I"
        # 47Humanities Elective Course II
        elif subjects == "Humanities Elective Course II":
            Result = "The subject hasn't other subjects to connect the flow"
        # 48Computer Eng. Elective Course III
        elif subjects == "Computer Eng. Elective Course III":
            Result = "Computer Eng. Elective Course IV"
        # 49Computer Eng. Elective Course IV
        elif subjects == "Computer Eng. Elective Course IV":
            Result = "The subject hasn't other subjects to connect the flow"
        # 50ProjectII
        elif subjects == "Project II":
            Result = "The subject hasn't other subjects to connect the flow"
        # 51Computer Eng. Seminar
        elif subjects == "Computer Eng. Seminar":
            Result = "The subject hasn't other subjects to connect the flow"
        # 52Free Elective Course II
        elif subjects == "Free Elective Course II":
            Result = "The subject hasn't other subjects to connect the flow"
        # 53Science and Maths Elective III
        elif subjects == "Science and Maths Elective III":
            Result = "The subject hasn't other subjects to connect the flow"
        # Other
        else:
            Result = "The subject isn't in the flow"

    return render(request, 'flow.html', {'subjects': subjects, 'Result': Result})


def listOfSubject(request):
    # list of semister subjects
    listSemister1 = """ Programming Fundamental<br />
            Engineering Mathematics I<br />
            Computer Engineering Exploration<br />
            Physics I<br />
            Physics Laboratory I<br />
            Language Elective Course I<br />
            Physical Education Elective Course I<br />
            Social Sciences Elective Course<br />
            Introduction to Engineer<br />"""

    listSemister2 = """Electric Circuit Theory<br />
            Electric Circuit Lab<br />
            Algorithms and Data Structure<br />
            Work Ethics<br />
            Engineering Mathematics II<br />
            Physics II<br />
            Physics Laboratory II<br />
            Language Elective Course II<br />
            Physical Education Elective Course II<br />"""

    listSemister3 = """Statistics for Computer Engineer<br />
            Introduction to Signals and System<br />
            Logic Design of Digital System<br />
            Digital System Design Laboratory<br />
            Software Development Practice I<br />
            Discrete Mathematics<br />
            Science and Maths Elective I<br />"""

    listSemister4 = """Software Development Practice II<br />
            Computer Networks I<br />
            Computer Organization<br />
            Ubiquitous Computing<br />
            Analog and Digital Electronics<br />
            Science and Maths Elective II<br />"""

    listSemister5 = """Software Engineering<br />
            Computer Networks II<br />
            Operating Systems<br />
            Embedded System Design<br />
            Analog and Digital Electronics Lab<br />
            Language Elective Course III<br />"""

    listSemister6 = """Database Systems<br />
            Computer Networks Lab<br />
            Embedded System Design Laboratory<br />
            Language Elective Course IV<br />
            Computer Eng. Elective Course I<br />
            Computer Eng. Elective Course II<br />
            Humanities Elective Course I<br />"""

    listSemister7 = """Project I<br />
            Free Elective Course I<br />
            Humanities Elective Course II<br />
            Computer Eng. Elective Course III<br />
            Computer Eng. Elective Course IV<br />"""

    listSemister8 = """Project II<br />
            Computer Eng. Seminar<br />
            Free Elective Course II<br />
            Science and Maths Elective III"""
    # return listsubjects for each semester
    return render(request, 'subject.html',
                  {'semister1': listSemister1, 'semister2': listSemister2, 'semister3': listSemister3,
                   'semister4': listSemister4, 'semister5': listSemister5, 'semister6': listSemister6,
                   'semister7': listSemister7, 'semister8': listSemister8})


def Graph(request):
    # create countunit and GPAX var
    countunit = 0
    GPAX = 0
    # collect each term data to var
    dataterm_1 = Term1.objects.all()
    dataterm_2 = Term2.objects.all()
    dataterm_3 = Term3.objects.all()
    dataterm_4 = Term4.objects.all()
    dataterm_5 = Term5.objects.all()
    dataterm_6 = Term6.objects.all()
    dataterm_7 = Term7.objects.all()
    dataterm_8 = Term8.objects.all()
    dataGPA = GPA.objects.all()
    countunit = 0
    # if GPA is empty create (gpa1-gpa8)
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        # sum for GPAX
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(
            i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        # if unit in GPAX not equal to 0 countunit will add1
        for unit in dataGPA:
            if unit.GPA_1 != "0":
                countunit += 1
            if unit.GPA_2 != "0":
                countunit += 1
            if unit.GPA_3 != "0":
                countunit += 1
            if unit.GPA_4 != "0":
                countunit += 1
            if unit.GPA_5 != "0":
                countunit += 1
            if unit.GPA_6 != "0":
                countunit += 1
            if unit.GPA_7 != "0":
                countunit += 1
            if unit.GPA_8 != "0":
                countunit += 1
    else:
        countunit += 1
    # calculate GPAX
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    # return graph.html (dataterm_each_term, gpa, gpax)
    return render(request, 'Graph.html', {'dataterm1': dataterm_1, 'dataterm2': dataterm_2, 'dataterm3': dataterm_3,
                                          'dataterm4': dataterm_4, 'dataterm5': dataterm_5, 'dataterm6': dataterm_6,
                                          'dataterm7': dataterm_7, 'dataterm8': dataterm_8, 'GPARES': dataGPA,
                                          'res_GPAX': newGPAX})


def Result(request):
    # create dataGPA to collect gpa var
    dataGPA = GPA.objects.all()
    # if dataGPA is empty create new one (from gpa1 - gpa8)
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    # collect object to dataterm var
    # collect gpa to dataGPA var
    dataterm_1 = Term1.objects.all()
    dataterm_2 = Term2.objects.all()
    dataGPA = GPA.objects.all()
    # return result.html (dataterm and gpa)
    return render(request, 'Result.html', {'dataterm1': dataterm_1, 'dataterm2': dataterm_2, 'GPARES': dataGPA})


def firstTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_1 = Term1.objects.all()
    countunit = 0
    # if GPA is empty create (gpa1-gpa8)
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        # sum for GPAX
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(
            i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        # if unit in GPAX not equal to 0 countunit will add1
        for unit in dataGPA:
            if unit.GPA_1 != "0":
                countunit += 1
            if unit.GPA_2 != "0":
                countunit += 1
            if unit.GPA_3 != "0":
                countunit += 1
            if unit.GPA_4 != "0":
                countunit += 1
            if unit.GPA_5 != "0":
                countunit += 1
            if unit.GPA_6 != "0":
                countunit += 1
            if unit.GPA_7 != "0":
                countunit += 1
            if unit.GPA_8 != "0":
                countunit += 1
    else:
        # calculate GPAX
        countunit += 1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    # return graph.html (dataterm_each_term, gpa, gpax)
    return render(request, 'firstTerm.html', {'dataterm1': dataterm_1, 'GPARES': dataGPA, 'res_GPAX': newGPAX})


def secondTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_2 = Term2.objects.all()
    countunit = 0
    # if GPA is empty create (gpa1-gpa8)
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        # sum for GPAX
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(
            i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        # if unit in GPAX not equal to 0 countunit will add1
        for unit in dataGPA:
            if unit.GPA_1 != "0":
                countunit += 1
            if unit.GPA_2 != "0":
                countunit += 1
            if unit.GPA_3 != "0":
                countunit += 1
            if unit.GPA_4 != "0":
                countunit += 1
            if unit.GPA_5 != "0":
                countunit += 1
            if unit.GPA_6 != "0":
                countunit += 1
            if unit.GPA_7 != "0":
                countunit += 1
            if unit.GPA_8 != "0":
                countunit += 1
    else:
        countunit += 1
        # calculate GPAX
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    # return graph.html (dataterm_each_term, gpa, gpax)
    return render(request, 'secondTerm.html', {'dataterm2': dataterm_2, 'GPARES': dataGPA, 'res_GPAX': newGPAX})


def thirdTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_3 = Term3.objects.all()
    countunit = 0
    # if GPA is empty create (gpa1-gpa8)
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        # sum for GPAX
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(
            i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        # if unit in GPAX not equal to 0 countunit will add1
        for unit in dataGPA:
            if unit.GPA_1 != "0":
                countunit += 1
            if unit.GPA_2 != "0":
                countunit += 1
            if unit.GPA_3 != "0":
                countunit += 1
            if unit.GPA_4 != "0":
                countunit += 1
            if unit.GPA_5 != "0":
                countunit += 1
            if unit.GPA_6 != "0":
                countunit += 1
            if unit.GPA_7 != "0":
                countunit += 1
            if unit.GPA_8 != "0":
                countunit += 1
    else:
        countunit += 1
        # calculate GPAX
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    # return graph.html (dataterm_each_term, gpa, gpax)
    return render(request, 'thirdTerm.html', {'dataterm3': dataterm_3, 'GPARES': dataGPA, 'res_GPAX': newGPAX})


def fourthTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_4 = Term4.objects.all()
    countunit = 0
    # if GPA is empty create (gpa1-gpa8)
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        # sum for GPAX
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(
            i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        # if unit in GPAX not equal to 0 countunit will add1
        for unit in dataGPA:
            if unit.GPA_1 != "0":
                countunit += 1
            if unit.GPA_2 != "0":
                countunit += 1
            if unit.GPA_3 != "0":
                countunit += 1
            if unit.GPA_4 != "0":
                countunit += 1
            if unit.GPA_5 != "0":
                countunit += 1
            if unit.GPA_6 != "0":
                countunit += 1
            if unit.GPA_7 != "0":
                countunit += 1
            if unit.GPA_8 != "0":
                countunit += 1
    else:
        countunit += 1
        # calculate GPAX
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    # return graph.html (dataterm_each_term, gpa, gpax)
    return render(request, 'fourthTerm.html', {'dataterm4': dataterm_4, 'GPARES': dataGPA, 'res_GPAX': newGPAX})


def fifthTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_5 = Term5.objects.all()
    countunit = 0
    # if GPA is empty create (gpa1-gpa8)
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        # sum for GPAX
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(
            i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        # if unit in GPAX not equal to 0 countunit will add1
        for unit in dataGPA:
            if unit.GPA_1 != "0":
                countunit += 1
            if unit.GPA_2 != "0":
                countunit += 1
            if unit.GPA_3 != "0":
                countunit += 1
            if unit.GPA_4 != "0":
                countunit += 1
            if unit.GPA_5 != "0":
                countunit += 1
            if unit.GPA_6 != "0":
                countunit += 1
            if unit.GPA_7 != "0":
                countunit += 1
            if unit.GPA_8 != "0":
                countunit += 1
    else:
        # calculate GPAX
        countunit += 1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    # return graph.html (dataterm_each_term, gpa, gpax)
    return render(request, 'fifthTerm.html', {'dataterm5': dataterm_5, 'GPARES': dataGPA, 'res_GPAX': newGPAX})


def sixthTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_6 = Term6.objects.all()
    countunit = 0
    # if GPA is empty create (gpa1-gpa8)
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        # sum for GPAX
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(
            i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        # if unit in GPAX not equal to 0 countunit will add1
        for unit in dataGPA:
            if unit.GPA_1 != "0":
                countunit += 1
            if unit.GPA_2 != "0":
                countunit += 1
            if unit.GPA_3 != "0":
                countunit += 1
            if unit.GPA_4 != "0":
                countunit += 1
            if unit.GPA_5 != "0":
                countunit += 1
            if unit.GPA_6 != "0":
                countunit += 1
            if unit.GPA_7 != "0":
                countunit += 1
            if unit.GPA_8 != "0":
                countunit += 1
    else:
        # calculate GPAX
        countunit += 1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    # return graph.html (dataterm_each_term, gpa, gpax)
    return render(request, 'sixthTerm.html', {'dataterm6': dataterm_6, 'GPARES': dataGPA, 'res_GPAX': newGPAX})


def seventhTerm(request):
    dataterm_7 = Term7.objects.all()
    dataGPA = GPA.objects.all()
    countunit = 0
    # if GPA is empty create (gpa1-gpa8)
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        # sum for GPAX
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(
            i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        # if unit in GPAX not equal to 0 countunit will add1
        for unit in dataGPA:
            if unit.GPA_1 != "0":
                countunit += 1
            if unit.GPA_2 != "0":
                countunit += 1
            if unit.GPA_3 != "0":
                countunit += 1
            if unit.GPA_4 != "0":
                countunit += 1
            if unit.GPA_5 != "0":
                countunit += 1
            if unit.GPA_6 != "0":
                countunit += 1
            if unit.GPA_7 != "0":
                countunit += 1
            if unit.GPA_8 != "0":
                countunit += 1
    else:
        # calculate GPAX
        countunit += 1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    # return graph.html (dataterm_each_term, gpa, gpax)
    return render(request, 'seventhTerm.html', {'dataterm7': dataterm_7, 'GPARES': dataGPA, 'res_GPAX': newGPAX})


def eightTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_8 = Term8.objects.all()
    countunit = 0
    # if GPA is empty create (gpa1-gpa8)
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        # sum for GPAX
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(
            i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        # if unit in GPAX not equal to 0 countunit will add1
        for unit in dataGPA:
            if unit.GPA_1 != "0":
                countunit += 1
            if unit.GPA_2 != "0":
                countunit += 1
            if unit.GPA_3 != "0":
                countunit += 1
            if unit.GPA_4 != "0":
                countunit += 1
            if unit.GPA_5 != "0":
                countunit += 1
            if unit.GPA_6 != "0":
                countunit += 1
            if unit.GPA_7 != "0":
                countunit += 1
            if unit.GPA_8 != "0":
                countunit += 1
    else:
        countunit += 1
        # calculate GPAX
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    # return graph.html (dataterm_each_term, gpa, gpax)
    return render(request, 'eightTerm.html', {'dataterm8': dataterm_8, 'GPARES': dataGPA, 'res_GPAX': newGPAX})


def picFlow(request):
    # return picFlow.html page
    return render(request, 'picFlow.html')


def about(request):
    # return about.html page
    return render(request, 'about.html')


def help(request):
    return render(request, 'help.html')
