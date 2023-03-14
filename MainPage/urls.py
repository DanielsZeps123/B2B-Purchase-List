"""Project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'main_page'
urlpatterns = [
    path('business', views.mainPage, name='business'),
    path('business/<int:business>', views.business, name='page'),
    path('sell', views.mainPage, name='sell'),
    path('buy', views.mainPage, name='buy'),
    path('login', views.login, name='login'),
    path('checkLogin', views.checkLogin, name='checkLogin'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('editProfile', views.editProfile, name='editProfile'),
    path('updateProfile', views.updateProfile, name='updateProfile'),
    path('products', views.products, name='products'),
    
]
