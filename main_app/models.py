# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Profile(models.Model):
    GENDER_OPTIONS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='static/img/profile_pictures', blank=True, verbose_name='Profile Picture')
    country = models.TextField(max_length=30, verbose_name="Country")
    city = models.TextField(max_length=30, verbose_name="City")
    gender = models.TextField(choices=GENDER_OPTIONS, max_length=7, verbose_name="Gender")
    birth_date = models.DateTimeField(auto_now_add=True, verbose_name="Birth date")



class Wish(models.Model):

    PRIVACY_OPTIONS = (
        ('Public', 'Public'),
        ('Friends', 'Friends'),
        ('Private', 'Private'),
    )

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.TextField(max_length=120, verbose_name="title")
    picture = models.ImageField(upload_to='static/img/wish_pics', blank=True, verbose_name='Wish Picture')
    details = models.TextField(max_length=350, verbose_name="Details")
    url = models.TextField(max_length=255, verbose_name="Wish URL")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    added_by = models.ForeignKey(User, max_length=50, verbose_name="Added by", null=False, on_delete=models.CASCADE)
    privacy = models.TextField(choices=PRIVACY_OPTIONS, max_length=20, verbose_name="Wish Privacy")



class Event(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    event = models.TextField(max_length=120, verbose_name="Event")
    event_date = models.DateTimeField(auto_now_add=True, verbose_name="Event Date")


class Country(models.Model):
    pass

class City(models.Model):
    pass