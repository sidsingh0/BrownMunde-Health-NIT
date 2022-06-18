from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="health-home"),
    path('tracker/', views.tracker, name="health-tracker"),
    path('appointment/', views.appointment, name="health-appointment"),
    path('picker/', views.picker, name="health-picker"),
    path('signup/', views.handleSignup, name="health-signup"),
    path('login/', views.handleLogin, name="health-login"),
    path('logout/', views.handleLogout, name="health-logout"),
]
