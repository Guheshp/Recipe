from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import Receipe, ReceipReview

from django.db.models import Avg

from .form import (CreateReceipForm,
                    ReviweForm,
                    UpdateReceipeFprm, )
# Create your views here.

@login_required(login_url='my-login')
def All_Receipe(request):

    queryset = Receipe.objects.filter().order_by('-created_at')

    context = {'Receipe':queryset}

    return render(request,'receipe/all_receipe.html',context)


def UpdateReceipe(request, pk):

    receip = Receipe.objects.get(id=pk)

    form = UpdateReceipeFprm(instance=receip)

    if request.method == 'POST':

        form = UpdateReceipeFprm(request.POST, instance=receip)

        if form.is_valid():

            form.save()

            messages.success(request, 'Successfully receipeform updated')

            return redirect('my-all_receipe')

    context = {'form':form,"receip":receip }
    return render(request, 'receipe/update_receipe.html', context)



@login_required(login_url='my-login')
def Food(request):
    if request.method == "POST":

        data = request.POST

        receipe_name  = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receip_image')
        receipe_price = data.get('receipe_price')

        Receipe.objects.create(
            receipe_name= receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
            receipe_price=receipe_price,
        )
        return redirect('my-all_receipe')
    
   
    
    return render(request, 'receipe/receipe.html')

@login_required(login_url='my-login')
def ReceipeView(request, pk):

    receip = Receipe.objects.get(id=pk)

    # getting all review
    review = ReceipReview.objects.filter(receipe=receip)

    context = {'receip':receip, 'review':review}

    return render(request, 'receipe/receipe_view.html', context)


@login_required(login_url='my-login')
def CreateReview(request, receip_id):

    url = request.META.get("HTTP_REFERER")

    if request.method == "POST":

        try:
            reviews = ReceipReview.objects.get(user__id=request.user.id, receipe__id= receip_id)

            form = ReviweForm(request.POST, instance=reviews)

            form.save()

            messages.success(request, 'Thank you, Your review has been updated')

            return redirect(url)

        except ReceipReview.DoesNotExist:

            form = ReviweForm(request.POST)

            if form.is_valid():
                data = ReceipReview()
                data.review = form.cleaned_data['review']
                data.rating = form.cleaned_data['rating']
                data.receipe = Receipe.objects.get(pk=receip_id)
                data.user = request.user
                data.save()
                messages.success(request, 'Thank you, Your review has been Created')
                return redirect(url)


    


    

# @login_required(login_url='my-login')
# def CreateReview(request, pk):

#     receipes = Receipe.objects.get(id=pk)

#     form = ReviweForm()
   

#     if request.method == "POST":

#         form = ReviweForm(request.POST)

#         if form.is_valid():

#             review = form.save(commit=False)
#             review.receipe = receipes
#             review.save()

#             messages.success(request, "Your record was Created!")

#             return redirect("my-all_receipe")
#         else:
               
#                form = ReviweForm()
    
#     context = {'review': form,  'receipes': receipes}

#     return redirect(request, 'receipe/create_review.html', context)