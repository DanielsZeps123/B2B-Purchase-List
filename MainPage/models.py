from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=50, default=None)
    business = models.BooleanField(default=False)
    sell = models.BooleanField(default=False)
    buy = models.BooleanField(default=False)

    def __str__(self):
        return str(self.tag) + " - " + str(self.business) + " " + str(self.sell) + " " + str(self.buy)

class Request(models.Model):
    address = models.CharField(max_length=100, default=None)
    product = models.CharField(max_length=100, default=None)
    phone = models.CharField(max_length=20, default=None)
    #Image field
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(default=None)

    def __str__(self):
        return str(self.product)

class Sell(Request):
    price = models.FloatField(default=None)

class Buy(Request):
    pass

class Business(models.Model):
    title = models.CharField(max_length=100, default=None)
    surname = models.CharField(max_length=100, default=None)
    name = models.CharField(max_length=100, default=None)
    login = models.DateTimeField(default=None)
    address = models.CharField(max_length=100, default=None)
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE, default=None)
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE, default=None)

class Users(models.Model):
    password = models.CharField(max_length=100, default=None)
    eMail = models.EmailField(default=None)
    busines = models.ForeignKey(Business, on_delete=models.CASCADE, default=None)

# Create your models here.
