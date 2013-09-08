# coding: utf-8

from django.template import render


def homepage(request):
    return render(request, 'index.html')
