from django.urls import path

from . import views 

urlpatterns = [

    # path('', views. ReceipeHome, name='my-r_home'),
    path('', views.Food, name='my-r_receip'),
    path('all_receipe/', views.All_Receipe, name='my-all_receipe'),
    path('receipe_view/<int:pk>', views.ReceipeView, name='my-receipe_view'),
    path('update_receipe/<int:pk>', views.UpdateReceipe, name='my-update_receipe'),
    
    path('review/<int:receip_id>/', views.CreateReview, name='my-review'),
   

]