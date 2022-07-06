from django.contrib import admin

# Register your models here.

from .models import (Continent, Country, Cities, Subscription, API)

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Cities)
admin.site.register(Subscription)
admin.site.register(API)
