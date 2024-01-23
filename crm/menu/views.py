from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import Receipe

from .form import (CreateReceipForm, )
# Create your views here.

@login_required(login_url='my-login')
def All_Receipe(request):

    queryset = Receipe.objects.all()

    context = {'Receipe':queryset}

    return render(request,'receipe/all_receipe.html',context)

@login_required(login_url='my-login')
def Food(request):
    if request.method == "POST":

        data = request.POST

        receipe_name  = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receip_image')

        Receipe.objects.create(
            receipe_name= receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )
        return redirect('my-all_receipe')
    
    return render(request, 'receipe/receipe.html')

@login_required(login_url='my-login')
def ReceipeView(request, pk):

    queryset = Receipe.objects.get(id=pk)

    context = {'receip':queryset}


    return render(request, 'receipe/receipe_view.html', context)