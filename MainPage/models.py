from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=50, default=None)
    business = models.BooleanField(default=True)
    sell = models.BooleanField(default=True)
    buy = models.BooleanField(default=True)

    def __str__(self):
        return str(self.tag) + " - " + str(self.business) + " " + str(self.sell) + " " + str(self.buy)

class Request(models.Model):
    address = models.CharField(max_length=100, default=None, blank=True, null=True)
    product = models.CharField(max_length=100, default=None, blank=True, null=True)
    phone = models.CharField(max_length=20, default=None, blank=True, null=True)
    image = models.ImageField(upload_to ='MainPage/static/images/', blank=True, null=True)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None, blank=True, null=True)
    date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.product)

class Sell(Request):
    price = models.FloatField(default=None, blank=True, null=True)

class Buy(Request):
    pass

class Business(models.Model):
    title = models.CharField(max_length=100, default=None, blank=True, null=True)
    surname = models.CharField(max_length=100, default=None, blank=True, null=True)
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    login = models.DateTimeField(default=None, blank=True, null=True)
    address = models.CharField(max_length=100, default=None, blank=True, null=True)
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE, default=None, blank=True, null=True)
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE, default=None, blank=True, null=True)
    
    def __str__(self):
        return str(self.title) + " " + str(self.name) + " " + str(self.surname)

class User(Business):
    password = models.CharField(max_length=100, default=None)
    eMail = models.EmailField(default=None)

    def __str__(self):
        return super().__str__()

# Create your models here.
