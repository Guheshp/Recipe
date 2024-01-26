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

from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model
from django.http import HttpResponse

from django.contrib.auth import get_user_model

# Create your views here.

# home.

def Home(request):
    # my_records = Record.objects.all()

    # context = {'records' : my_records}

    return render(request, 'webapp/index.html')

# user register.

def Register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

        # If the form is valid, create a new user instance but don't save it to the database immediately
            user = form.save(commit=False)

        # Set the 'is_active' attribute of the user to False
            user.is_active = False

        # Save the user instance with the 'is_active' set to False
            user.save()
        
        # Get the current site's domain
            current_site = get_current_site(request)  

        # Prepare the email subject and message for account activation
            mail_subject = 'Activation link has been sent to your email id'   
            message = render_to_string('webapp/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
        # Get the email address from the form
            to_email = form.cleaned_data.get('email')  
        # Create an EmailMessage instance
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )
         # Send the activation email
            email.send()

            messages.success(request, "Please confirm your email address to complete the registration ")

            return redirect('my-login')
        
        else:

            form = CreateUserForm()

            context = {'form':form}

            return render(request, 'webapp/register.html',context=context)
  
    return render(request, 'webapp/register.html')
       
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


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect('my-acc_active_email_complete')
    else:  
       return redirect('my-acc_active_email_invalid') 
    

def acc_active_email_complete(request):
    return render(request, 'webapp/acc_active_email_complete.html')
    

def acc_active_email_invalid(request):
    return render(request, 'webapp/acc_active_email_invalid.html')



          
    

