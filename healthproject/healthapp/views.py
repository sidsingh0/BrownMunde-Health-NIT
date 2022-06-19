from django.shortcuts import render, redirect
from newsapi import NewsApiClient
from django.contrib import messages
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from . models import *
import pandas as pd
import datetime
import plotly
import json
import plotly.express as px
import requests
from django.contrib.auth.decorators import login_required

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "qBp83gL97z1g8EHhK6ipU1MZuEfEOw8J"
NEWS_API_KEY = "b52c3bd64a744b7cbb7e05e997668ecf"
APPLICATION_ID = "4d9357ff"
API_KEY = "e4171aca238375ab4d3a135d772c8a4d"
nutri_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": API_KEY,
}
# Create your views here.


def home(request):
    response = requests.get("https://zenquotes.io/api/today/[your_key]%22")
    data = response.json()
    quote = (data[0]['q'])
    author = (data[0]['a'])
    newsapi = NewsApiClient(api_key='b52c3bd64a744b7cbb7e05e997668ecf')
    top_headlines = newsapi.get_top_headlines(category='health',
                                              language='en',
                                              country='in')
    news = []
    for n in range(0, 3):
        articles = [top_headlines['articles'][n]['title'], top_headlines['articles'][n]['description'],
                    top_headlines['articles'][n]['url'], top_headlines['articles'][n]['urlToImage']]
        news.append(articles)
    return render(request, 'healthapp/home.html', {'news': news, 'quote': quote, 'author': author})


def handleSignup(request):
    if request.method == "POST":
        username = request.POST.get("name", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        if not username.isalnum():
            messages.error(request, 'Your username must only contain letters and numbers!')
            return redirect("/")
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect("/")
        try:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            messages.success(request, 'Your account has been created successfully! Login Now!')
        except:
            messages.error(request, 'Your username must be unique! Please sign up again.')
        return redirect("/")
    else:
        return HttpResponseNotFound("<h1>404 - Forbidden</h1>The requested URL is not allowed!")


def handleLogin(request):
    if request.method == "POST":
        username = request.POST.get("name", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Invalid credentials!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseNotFound("<h1>404 - Forbidden</h1>The requested URL is not allowed!")


@login_required(login_url="/")
def handleLogout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, 'Successfully Logged out!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="/")
def dashboard(request):
    if request.user.is_authenticated:
        cal_objs = Calorie.objects.filter(user=request.user).values('date', 'calorie_burnt')
        if cal_objs:
            df = pd.DataFrame(list(cal_objs))
            fig = px.bar(df, x=df['date'], y=df['calorie_burnt'], title=f"{request.user.username}'s Calorie Chart")
            graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            return render(request, 'healthapp/dashboard.html', {'cal_objs': cal_objs, 'graph': graph})
        else:
            return render(request, 'healthapp/dashboard.html')
    return redirect("/")


def appointment(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        desc = request.POST.get('desc')
        pincode = request.POST.get('pincode')
        appointment = Appointment.objects.create(user=request.user, full_name=full_name, email=email, phone=phone,
                                                 desc=desc, address=address, pincode=pincode)
        appointment.save()
        messages.success(request, "Your appointment has been booked successfully! You can view them below your profile as My Appointments!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'healthapp/appointment.html')


@login_required(login_url="/")
def get_appointments(request):
    if request.user.is_authenticated:
        my_appointments = Appointment.objects.filter(user=request.user)
        return render(request, "healthapp/my_appointments.html", {'my_appt': my_appointments})
    return redirect("/")


def picker(request):
    return render(request, 'healthapp/picker.html')


def bmi(request):
    if request.method == "POST":
        weight = float(request.POST.get("weight"))
        height = float(request.POST.get("height"))
        bmi = (weight/(height**2))*10000
        if bmi < 18.5:
            text = "warning"
            remarks = "Underweight"
        if 18.5 < bmi < 25:
            text = "success"
            remarks = "Healthy"
        if 25 < bmi < 30:
            text = "warning"
            remarks = "Overweight"
        if bmi >= 30:
            text = "danger"
            remarks = "Obese"
        return render(request, "healthapp/bmi.html", {'bmi': bmi, 'text': text, 'remarks': remarks})
    return render(request, "healthapp/bmi.html")


@login_required(login_url="/")
def tracker(request):
    if request.user.is_authenticated:
        done = True
        user_prev_cal = Calorie.objects.filter(user=request.user).order_by("-date")
        if user_prev_cal:
            prev_date = user_prev_cal[0].date
            date_today = datetime.datetime.now().date()
            if date_today > prev_date:
                done = False
        else:
            done = False
        if request.method == "POST":
            cal = float(request.POST.get("cal", "0.00"))
            if not cal:
                exercise_params = {
                    "query": request.POST.get("calnlp", ""),
                    "gender": "male",
                    "weight_kg": float(request.POST.get("weight", "0.00")),
                    "height_cm": float(request.POST.get("height", "0.00")),
                    "age": int(request.POST.get("age", "0"))
                }
                query = requests.post(url=nutri_api_endpoint, json=exercise_params, headers=headers)
                data = query.json()
                total_cal_burnt = 0
                total_mins_spent = 0
                exercises = []
                for n in range(0, len(data['exercises'])):
                    exercise = [data['exercises'][n]['name'].title(), data['exercises'][n]['nf_calories'],
                                data['exercises'][n]['duration_min']]
                    exercises.append(exercise)
                    total_cal_burnt = total_cal_burnt + data['exercises'][n]['nf_calories']
                    total_mins_spent = total_mins_spent + data['exercises'][n]['duration_min']
                cal_obj = Calorie.objects.create(calorie_burnt=total_cal_burnt, user=request.user)
                cal_obj.save()
                done=True
                messages.info(request, f"You've burnt {total_cal_burnt} calories and spent {total_mins_spent} minutes!")
                return render(request, 'healthapp/tracker.html', {'done': "true"})
            if not done:
                cal_obj = Calorie.objects.create(calorie_burnt=cal, user=request.user)
                cal_obj.save()
                messages.success(request, "Your calories for today has been recorded!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if done:
            return render(request, 'healthapp/tracker.html', {'done': "true"})
    else:
        return redirect("/")
    return render(request, 'healthapp/tracker.html')


def get_exercises(request, type):
    exercises = Exercise.objects.filter(type=type)
    return render(request, "healthapp/exercises.html", {'exercises': exercises, 'type': type})
