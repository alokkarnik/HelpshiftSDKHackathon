# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Order

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def orders(request):
    active_order_list = Order.objects.all()
    template = loader.get_template('bhukkad/orders.html')
    context = {
        'active_order_list': active_order_list
    }
    return HttpResponse(template.render(context, request))
