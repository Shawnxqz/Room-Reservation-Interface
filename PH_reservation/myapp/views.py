
from datetime import datetime
from unicodedata import category
from django.contrib import messages
from django.shortcuts import render
from decimal import Decimal

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Classroom, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


def home(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/home.html')
    else:
        return render(request, 'myapp/signin.html')


@login_required(login_url='signin')
def findClassroom(request):
    context = {}
    if request.method == 'POST':
        # try:
        category_r = request.POST.get('category')
        # dest_r = request.POST.get('destination')


        search_room = request.POST.get('searchClassroom')
        numberStudent = int(request.POST.get('sizeOfRoom'))
        noise_front =request.POST.getlist('noise')


        if search_room is None:
            classroom_list = Classroom.objects.filter(status='available',capacity__gte=numberStudent,noise=noise_front[0])
        else:
            classroom_list = Classroom.objects.filter(classroom_name=search_room)
         



            

        # classroom_list = Classroom.objects.filter(category=category_r, dest=dest_r, date__year=year, date__month=month, date__day=day)
        if classroom_list:
            return render(request, 'myapp/list.html', locals())
        else:
            context['data'] = request.POST
            context["error"] = "No available Classroom"
            return render(request, 'myapp/findclassroom.html', context)
        # catch:
        #     search_room = request.POST.get('searchClassroom')
        #     if search_room != '':
        #         classroom_list = Classroom.objects.filter(classroom_name=search_room)
        #         return render(request, 'myapp/list.html', locals())
        #     else:
        #         context['data'] = request.POST
        #         context["error"] = "No available Classroom"
        #         return render(request, 'myapp/findclassroom.html', context)
    else:
        return render(request, 'myapp/findclassroom.html')


@login_required(login_url='signin')
def bookings(request):
    context = {}
    if request.method == 'POST':

        data_r = request.POST.get('classroom_name,numberStudent')
        name_r = data_r.split(",")[0]
        numStudent = int(data_r.split(",")[1])

        classroom = Classroom.objects.get(classroom_name=name_r)
        if classroom:
            category_r = classroom.category
            name_r = classroom.classroom_name
            status_r = classroom.status
            energyEfficiency_r = classroom.energyEfficiency
            capacity_r = classroom.capacity
            
            andrewid_r = request.user.username
            email_r = request.user.email
            userid_r = request.user.id
            

            
            book = Book.objects.create(andrewid=andrewid_r, email=email_r, userid=userid_r, classroom_name=name_r,

                                        category=category_r, book_status='BOOKED', capacity=capacity_r, energyEfficiency=energyEfficiency_r)
            curNum = classroom.number_student + numStudent
            Classroom.objects.filter(classroom_name=name_r).update(number_student=curNum)
            print('------------book id-----------', book.id)
            # book.save()
            return render(request, 'myapp/bookings.html', locals())

    else:
        return render(request, 'myapp/findclassroom.html')


@login_required(login_url='signin')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = 1
        try:
            id_r = request.POST.get('book_id')
            print(id_r)
        except ValueError:
            context["error"] = "Input not valid"
            return render(request, 'myapp/error.html', context)

        try:
            book = Book.objects.get(id=id_r)
            classroom = Classroom.objects.get(classroom_name=book.classroom_name)


            Book.objects.filter(id=id_r).update(book_status='CANCELLED')
            messages.success(request, "Booked Classroom has been cancelled successfully.")
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that classroom"
            return render(request, 'myapp/error.html', context)
        
    else:
        return render(request, 'myapp/findclassroom.html')


@login_required(login_url='signin')
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'myapp/booklist.html', locals())
    else:
        context["error"] = "Sorry no classroomes booked"
        return render(request, 'myapp/findclassroom.html', context)


def signup(request):
    context = {}
    if request.method == 'POST':
        andrewid_r = request.POST.get('andrewid')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(andrewid_r, email_r, password_r, )
        if user:
            login(request, user)
            return render(request, 'myapp/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signup.html', context)
    else:
        return render(request, 'myapp/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        andrewid_r = request.POST.get('andrewid')
        password_r = request.POST.get('password')
        user = authenticate(request, username=andrewid_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = andrewid_r
            context["id"] = request.user.id
            return render(request, 'myapp/success.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'myapp/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'myapp/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'myapp/success.html', context)
