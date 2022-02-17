from. import views
from django.urls import path,include
urlpatterns = [
    path("",views.signin_ups,name="login"),
    path("otp/", views.otp, name="login_otp"),
    path('send_otp',views.send_otp,name='send_otp'),
    path('logout',views.user_logout,name="logout"),
]
 
