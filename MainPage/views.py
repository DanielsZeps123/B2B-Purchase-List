from django.http import HttpResponse
from django.shortcuts import render

from .models import *

def mainPage(request, val):
    context = {
        'sections': Section.objects.all().values(
            'section',
            'id'
        ),
        'filter': Filter.objects.filter(section=val).values(),
    }
    return render(request, 'mainPage.html', context)

# Create your views here.
