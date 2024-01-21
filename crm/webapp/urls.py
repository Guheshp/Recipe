from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.Home, name=''),
    path('register', views.Register, name='my-register'),
    path('login', views.Login, name='my-login'),
    path('logout', views.Logout, name='my-logout'),
    path('dashboard', views.Dashboard, name='my-dashboard'),
    path('createrecord', views.CreateRecord, name='my-createrecord'),
    path('viewrecord/<int:pk>', views.Viewrecord, name='my-viewrecord'),
    path('updaterecord/<int:pk>', views.UpdateRecord, name='my-updaterecord'),
    path('deleteRecord/<int:pk>', views.DeleteRecord, name='my-deleteRecord'),

    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
#   path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),

     path('acc_active_email_complete',views.acc_active_email_complete, name='my-acc_active_email_complete'),

     path('acc_active_email_invalid',views.acc_active_email_invalid, name='my-acc_active_email_invalid'),
        

    path('reset_password', auth_views.PasswordResetView.as_view(template_name="webapp/reset_password.html" ), 
         name = 'reset_password'),

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="webapp/password_reset_done.html"), 
         name = 'password_reset_done'),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="webapp/password_reset_confirm.html"), 
         name = 'password_reset_confirm'),

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="webapp/password_reset_complete.html"), 
         name = 'password_reset_complete'),
  

]