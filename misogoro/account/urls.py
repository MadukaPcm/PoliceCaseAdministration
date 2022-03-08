from django.urls import path
from . import views

#path urls for expert app.
urlpatterns = [
    path('',views.HomepageView, name='homepage_url'),
    path('login/',views.LoginView, name='login_url'),
    path('LOGOUT/', views.LogoutView, name='logout_url'),
    path('register/',views.RegisterView, name='register_url'),
    path('forgotpassword/',views.ForgotPasswordView, name='forgotpassword_url'),

]