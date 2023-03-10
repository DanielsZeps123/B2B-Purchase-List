from django.contrib import admin

from .models import *

admin.site.register(Tag)
admin.site.register(Request)
admin.site.register(Sell)
admin.site.register(Buy)
admin.site.register(Business)
admin.site.register(User)
# Register your models here.
