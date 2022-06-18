from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'healthapp/home.html')
def tracker(request):
    return render(request,'healthapp/tracker.html',{"title":"Track your calories online"})
def appointment(request):
    return render(request,'healthapp/appointment.html',{"title":"Book an Appointment!"})