from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import *

def removePath(path):
    return path[path.find("/static")+7:]



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
            context['items'][x]["image"] = removePath(context['items'][x]["image"])
    elif end == "sell":
        context['items'] = Sell.objects.filter(public=True).values()
        for x in range(0, len(context['items'])):
            context['items'][x]["image"] = removePath(context['items'][x]["image"])
        context['tags'] = Tag.objects.filter(sell=True).values()
    elif end ==  "business":
        context['items'] = Business.objects.filter(public=True).values()
        context['tags'] = Tag.objects.filter(business=True).values()
        for x in range(0, len(context['items'])):
            context['items'][x]["image"] = removePath(context['items'][x]["background"])
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
        return HttpResponseRedirect('business')
    else:
        return render(request, 'loginPage.html', {})

def profile(request):
    context = {
        'background': removePath(request.session['user']['background']),
        'description': request.session['user']['description'],
        'longitude': request.session['user']['longitude'],
        'latitude': request.session['user']['latitude'],
        'address': request.session['user']['address'],
        'phone': request.session['user']['phone'],
        'title': request.session['user']['title'],
        'login': request.session['login'],
        'profile': True
    }
    return render(request, 'profile.html', context)

def editProfile(request):
    context = {
        'description': request.session['user']['description'],
        'longitude': request.session['user']['longitude'],
        'latitude': request.session['user']['latitude'],
        'surname': request.session['user']['surname'],
        'address': request.session['user']['address'],
        'public': request.session['user']['public'],
        'phone': request.session['user']['phone'],
        'title': request.session['user']['title'],
        'name': request.session['user']['name'],
        'login': request.session['login']
    }
    return render(request, 'editProfile.html', context)

def updateProfile(request):
    user = User.objects.get(pk=request.session['user']['id'])
    user.public = True if request.POST['public'] == "true" else False
    user.description = request.POST['description']
    user.longitude = request.POST['longitude']
    user.latitude = request.POST['latitude']
    user.surname = request.POST['surname']
    user.address = request.POST['address']
    user.phone = request.POST['phone']
    user.title = request.POST['title']
    user.name = request.POST['name']
    user.save()
    request.session['user'] = User.objects.filter(id=request.session['user']['id']).values()[0]
    return HttpResponseRedirect(reverse('main_page:profile'))

def products(request):
    return HttpResponseRedirect(reverse('main_page:business'))

def business(request, business):
    business = Business.objects.filter(pk=business).values()[0]
    context = {
        'background': removePath(business['background']),
        'description': business['description'],
        'longitude': business['longitude'],
        'login': request.session['login'],
        'latitude': business['latitude'],
        'address': business['address'],
        'phone': business['phone'],
        'title': business['title'],
        'profile': False
    }
    return render(request, 'profile.html', context)

def notExist(request):
    return render(request, 'profile.html', {})
# Create your views here.
