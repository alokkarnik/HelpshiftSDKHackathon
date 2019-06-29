# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=200)
    is_active = models.BooleanField(True)

class Food(models.Model):
    food_name = models.CharField(max_length=200)
    is_served = models.BooleanField(True)

class Order(models.Model):
    user = models.ForeignKey(User)
    food = models.ForeignKey(Food)
    quantity = models.PositiveIntegerField(default=1)
    status = models.PositiveIntegerField(default=0)
    instructions = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

class OrderHistory(models.Model):
    order = models.ForeignKey(Order)
    user = models.ForeignKey(User)
