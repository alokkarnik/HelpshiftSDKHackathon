# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class User(models.Model):
    user_name = models.CharField(max_length=200)
    is_active = models.BooleanField(True)

    def __str__(self):
        return '%s %d' % (self.user_name, self.is_active)
    

@python_2_unicode_compatible
class Food(models.Model):
    food_name = models.CharField(max_length=200)
    is_served = models.BooleanField(True)

    def __str__(self):
        return '%s %d' % (self.food_name, self.is_served)

@python_2_unicode_compatible
class Order(models.Model):
    user = models.ForeignKey(User)
    food = models.ForeignKey(Food)
    quantity = models.PositiveIntegerField(default=1)
    status = models.PositiveIntegerField(default=0)
    instructions = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %d %d %s %s' % (self.user.user_name, self.food.food_name, self.quantity, self.status, self.instructions, self.time)
