from django.db import models

class Business(models.Model):
    public = models.BooleanField(default=True)
    title = models.CharField(max_length=100, default=None, blank=True, null=True)
    login = models.DateTimeField(default=None, blank=True, null=True)
    phone = models.CharField(max_length=20, default=None, blank=True, null=True)
    address = models.CharField(max_length=100, default=None, blank=True, null=True)
    description = models.CharField(max_length=3000, default=None, blank=True, null=True)
    bussinesLogo = models.ImageField(upload_to ='MainPage/static/images/businesses/', blank=True, null=True)

    def __str__(self):
        return str(self.title)
    
class User(Business):
    password = models.CharField(max_length=100, default=None)
    eMail = models.EmailField(default=None)
    surname = models.CharField(max_length=100, default=None, blank=True, null=True)
    name = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return str(self.title) + " " + str(self.name) + " " + str(self.surname)

class Tag(models.Model):
    tag = models.CharField(max_length=50, default=None)
    business = models.BooleanField(default=True)
    sell = models.BooleanField(default=True)
    buy = models.BooleanField(default=True)

    def __str__(self):
        return str(self.tag) + " - " + str(self.business) + " " + str(self.sell) + " " + str(self.buy)

class Request(models.Model):
    public = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    order = models.ForeignKey(Business, on_delete=models.CASCADE, default=None, blank=True, null=True)
    address = models.CharField(max_length=100, default=None, blank=True, null=True)
    title = models.CharField(max_length=100, default=None, blank=True, null=True)
    phone = models.CharField(max_length=20, default=None, blank=True, null=True)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None, blank=True, null=True)
    date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.title)

class Sell(Request):
    image = models.ImageField(upload_to ='MainPage/static/images/sell/', blank=True, null=True)
    price = models.FloatField(default=None, blank=True, null=True)

class Buy(Request):
    image = models.ImageField(upload_to ='MainPage/static/images/buy', blank=True, null=True)
    pass

# Create your models here.
