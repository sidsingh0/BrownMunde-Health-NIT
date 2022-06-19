from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="health-home"),
    path('dashboard/', views.dashboard, name="health-dashboard"),
    path('tracker/', views.tracker, name="health-tracker"),
    path('appointment/', views.appointment, name="health-appointment"),
    path('picker/', views.picker, name="health-picker"),
    path('bmi/', views.bmi, name="health-bmi"),
    path('signup/', views.handleSignup, name="health-signup"),
    path('login/', views.handleLogin, name="health-login"),
    path('logout/', views.handleLogout, name="health-logout"),
    path('my-appointments/', views.get_appointments, name="health-my-appt"),
    path('<str:type>/exercises/', views.get_exercises, name="health-exercises"),
]
