from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import *

def mainPage(request):
    context = {
        'tags': Tag.objects.all().values() 
    }
    end = request.META['PATH_INFO']
    end = end[end.rfind("/")+1:]
    if end == "buy":
        context['tags'] = Tag.objects.filter(buy=True).values()
    elif end == "sell":
        context['tags'] = Tag.objects.filter(sell=True).values()
    elif end ==  "business":
        context['tags'] = Tag.objects.filter(business=True).values()
    return render(request, 'mainPage.html', context)

def logIn(request):
    return render(request, 'loginPage.html', {})

def checkLogin(request):

    try:
        user = request.GET['user']
    except:
        user = ""
    try:
        password = request.GET['password']
    except:
        password = ""

    users = Users.objects.filter(eMail=user, password=password).values()

    if len(users) == 1:
        request.session['user'] = users[0]
        request.session['login'] = True
        return HttpResponseRedirect('business')
    else:
        return render(request, 'loginPage.html', {})

# Create your views here.
