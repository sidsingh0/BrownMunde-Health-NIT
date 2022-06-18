from django.shortcuts import render, redirect
from newsapi import NewsApiClient
from django.contrib import messages
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from . models import *

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "qBp83gL97z1g8EHhK6ipU1MZuEfEOw8J"
NEWS_API_KEY = "b52c3bd64a744b7cbb7e05e997668ecf"
# Create your views here.


def home(request):
    newsapi = NewsApiClient(api_key='b52c3bd64a744b7cbb7e05e997668ecf')
    top_headlines = newsapi.get_top_headlines(category='health',
                                              language='en',
                                              country='in')
    news = []
    for n in range(0, 3):
        articles = [top_headlines['articles'][n]['title'], top_headlines['articles'][n]['description'],
                    top_headlines['articles'][n]['url'], top_headlines['articles'][n]['urlToImage']]
        news.append(articles)
    return render(request, 'healthapp/home.html', {'news': news})


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


def handleLogout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, 'Successfully Logged out!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def tracker(request):
    return render(request, 'healthapp/dashboard.html')


def appointment(request):
    return render(request, 'healthapp/appointment.html')


def picker(request):
    return render(request, 'healthapp/picker.html')
