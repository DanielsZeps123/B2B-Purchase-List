from django.http import HttpResponse
from django.shortcuts import render

def editData(request):
    return render(request, 'editData.html', {})

# Create your views here.
