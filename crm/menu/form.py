from django import forms
from .models import ReceipReview

from .models import (Receipe,
                     ReceipReview,
                    )


class CreateReceipForm(forms.ModelForm):

    class Meta:

        model = Receipe
        fields = ['receipe_name', 'receipe_description', 'receipe_image']
        

class ReviweForm(forms.ModelForm):

    class Meta:

        model = ReceipReview
        fields = ['review', 'rating']
        
class UpdateReceipeFprm(forms.ModelForm):

    class Meta:

        model = Receipe
        fields = ['receipe_name', 'receipe_description', 'receipe_image', 'receipe_price']