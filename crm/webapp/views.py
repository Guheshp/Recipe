from django.shortcuts import render, redirect
from django.http import HttpResponse

from . forms import (CreateUserForm,
                    LoginForm,
                    CreateRecordForm,
                    UpdateRecordForm,
                    )

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from . models import Record

from django.contrib import messages





# Create your views here.

# home.

def Home(request):
    return render(request, 'webapp/index.html')

# user register.

def Register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
             
            form.save()

            messages.success(request, "Account created successfully")

            return redirect('my-login')
        
    context = {'form':form}
  
    return render(request, 'webapp/register.html',context=context)
       
# user login.
def Login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data = request.POST) 

        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                auth.login(request, user)

                return redirect('my-dashboard')
          
    context = {'form':form}

    return render(request, 'webapp/login.html', context=context)

# user logout.

def Logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect('my-login')

# dashboard.

@login_required(login_url='my-login')
def Dashboard(request):

    my_records = Record.objects.all()

    context = {'records' : my_records}

    return render(request, 'webapp/dashboard.html', context=context)

# create a record 

@login_required(login_url='my-login')
def CreateRecord(request):
    
    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was Created!")

            return redirect("my-dashboard")
        
    context = {'form':form}

    return render(request, 'webapp/create-record.html', context=context)

# view record 
@login_required(login_url='my-login')
def Viewrecord(request, pk):
    
    record_all = Record.objects.get(id=pk)

    context = {'record_all': record_all}

    return render(request, 'webapp/view-record.html', context=context)

# update a record 

@login_required(login_url='my-signin')
def UpdateRecord(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was Updated!")

            return redirect("my-dashboard")
        
    context = {'form': form }

    return render(request, 'webapp/update-record.html', context=context)

@login_required(login_url='my-signin')
def DeleteRecord(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Deleted Successfylly!")

    return redirect('my-dashboard')


