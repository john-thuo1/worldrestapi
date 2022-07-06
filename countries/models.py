from tkinter import CASCADE
from django.db import models
from tabnanny import verbose

# User is the default Django user database table
from django.contrib.auth.models import User
# Create your models here.

# Continent Table Model
class Continent(models.Model):
    name = models.TextField(max_length=50)
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Continent(name='{self.name}')"
    
    class Meta:
        verbose_name_plural = 'Continents'

# Country Table Model
class Country(models.Model):
    continent = models.ForeignKey(Continent,on_delete=models.PROTECT,null=False)
    name = models.TextField(max_length=50)
    code = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Country(name='{self.name}',code='{self.code}')"
    
    class Meta:
        verbose_name_plural = 'Countries'

# Cities Table Model

class Cities(models.Model):
    name = models.TextField(max_length=50)
    # country = models.ForeignKey(Country, on_delete=CASCADE)
    country = models.ForeignKey(Country,on_delete=models.PROTECT,null=False)


    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Cities(country='{self.country}',name='{self.name}')"
    
    class Meta:
        verbose_name_plural = 'Cities'


class API(models.Model):
    name = models.TextField(max_length=50)
    code = models.CharField(max_length=5, null=True)

    def __str__(self):
        return f"{self.name} A.P.I."
    
    def __repr__(self):
        return f"API(name='{self.name}',code='{self.code}')"
    
    class Meta:
        verbose_name_plural = 'APIs'


class Subscription(models.Model):
    api = models.ForeignKey(API,on_delete=models.PROTECT,null=False)
    user = models.ForeignKey(User,on_delete=models.PROTECT,null=False)

    def __str__(self):
        return f"{self.user.username} : {self.api}"
    
    def __repr__(self):
        return f"Subscription(api='{self.api}',user='{self.user}')"
    
    class Meta:
        verbose_name_plural = 'Subscriptions'

