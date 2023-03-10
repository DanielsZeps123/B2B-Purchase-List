from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import *

def mainPage(request):
    context = {
        'tags': Tag.objects.all().values(),
        'items': None,
        'login': request.session['login']
    }
    end = request.META['PATH_INFO']
    end = end[end.rfind("/")+1:]
    if end == "buy":
        context['items'] = Buy.objects.filter(public=True).values()
        context['tags'] = Tag.objects.filter(buy=True).values()
        for x in range(0, len(context['items'])):
            context['items'][x]["image"] = "images/buy/" + context['items'][x]["image"][context['items'][x]["image"].rfind("/")+1:]
    elif end == "sell":
        context['items'] = Sell.objects.filter(public=True).values()
        for x in range(0, len(context['items'])):
            context['items'][x]["image"] = "images/sell/" + context['items'][x]["image"][context['items'][x]["image"].rfind("/")+1:]
        context['tags'] = Tag.objects.filter(sell=True).values()
    elif end ==  "business":
        context['items'] = Business.objects.filter(public=True).values()
        context['tags'] = Tag.objects.filter(business=True).values()
    return render(request, 'mainPage.html', context)

def login(request):
    return render(request, 'loginPage.html', {})

def logout(request):
    request.session['login'] = None
    request.session['user'] = None
    return HttpResponseRedirect('business')

def checkLogin(request):
    try: user = request.GET['user']
    except: user = ""
    try: password = request.GET['password']
    except: password = ""

    users = User.objects.filter(eMail=user, password=password).values()

    if len(users) == 1:
        request.session['user'] = users[0]
        request.session['login'] = True
        print(users[0])
        return HttpResponseRedirect('business')
    else:
        return render(request, 'loginPage.html', {})

def profile(request):
    context = {
        'description': request.session['user']['description'],
        'surname': request.session['user']['surname'],
        'address': request.session['user']['address'],
        'public': request.session['user']['public'],
        'phone': request.session['user']['phone'],
        'title': request.session['user']['title'],
        'name': request.session['user']['name']
    }
    return render(request, 'profile.html', context)

def updateProfile(request):
    user = User.objects.get(pk=request.session['user']['id'])
    user.public = True if request.POST['public'] == "true" else False
    user.description = request.POST['description']
    user.surname = request.POST['surname']
    user.address = request.POST['address']
    user.phone = request.POST['phone']
    user.title = request.POST['title']
    user.name = request.POST['name']
    user.save()
    request.session['user'] = User.objects.filter(id=request.session['user']['id']).values()[0]
    return HttpResponseRedirect(reverse('main_page:business'))

def notExist(request):
    return render(request, 'profile.html', {})
# Create your views here.
