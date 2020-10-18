from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Listing(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    website = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)
    business_hours = models.TextField()
    about = models.TextField()
    paid = models.BooleanField(default=False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
