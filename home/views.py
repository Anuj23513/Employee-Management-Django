from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.
def loginpage(request):

    if request.method=="POST":
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        validate_user=authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home')
        else:
             messages.error(request,'Wrong Credentials')
             return redirect('login')
        
    return render(request,'login.html')
@login_required(login_url="/")
def home(request):
    return render(request,'index.html')


@login_required(login_url="/")
def team(request):
    Employee_details=staff.objects.all().values()
    context={
        'Employee_details':Employee_details,
    }
    
    return render(request,'team.html',context)



@login_required(login_url='/')
def about(request):
    return render(request,'about.html')

@login_required(login_url='/')
def register(request):
    if request.method=="POST":
       
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        
        
        
        if len(password) < 4:
            messages.error(request,'Too short password')
            return redirect('register')
        
        get_all_user_by_username = User.objects.filter(username=username)
        if get_all_user_by_username:
             messages.error(request,'User already exists')
             return redirect('register')
         
        new_user = User.objects.create_user(username=username,email=email,password = password)
        new_user.save()
        messages.success(request,'User Created')
        return redirect('login')
        
  
            
    return  render(request,'register.html')

@login_required(login_url='/')
def contact(request):
    if request.method=="POST":
        form=request.POST
        name_contact=form.get('name_contact')
        phone_of_contact=form.get('phone_of_contact')
        email_of_contact=form.get('email_of_contact')
        address_of_contact=form.get('address_of_contact')
        subject_of_contact=form.get('subject_of_contact')
        message_of_contact=form.get('message_of_contact')
        
        contact_details.objects.create(
            name_contact=name_contact,
            phone_of_contact=phone_of_contact,
            email_of_contact=email_of_contact,
            address_of_contact=address_of_contact,
            subject_of_contact=subject_of_contact,
            message_of_contact=message_of_contact,    
        )
        messages.success(request,'Thank You,Your Response recorded successfully We will contact You shortly')
        return redirect('contact')
        
    
    return render(request,'contact.html')
@login_required(login_url='/')
def index(request):
    data = Employee.objects.all()
    context = {"data":data}
    return render(request,'job_dashboard.html',context)


@login_required(login_url='/')
def insertData(request):
    data = Employee.objects.all()
    context = {"data":data}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        query = Employee(name=name,email=email,gender=gender)
        query.save()
        return redirect('index')
    
    return render(request,"job_dashboard.html")
@login_required(login_url='/')
def updateData(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        edit = Employee.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.gender = gender

        edit.save()
       
        return redirect('/index')
    i = Employee.objects.get(id=id)
    context = {"i":i}
    return render(request,'edit.html',context)
@login_required(login_url='/')
def deleteData(request,id):
    d = Employee.objects.get(id=id)
    d.delete()
    return redirect('index')
  
   
  

