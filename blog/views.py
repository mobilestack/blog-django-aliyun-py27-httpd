# encoding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

def home(request):
    ctx = {}
    tmt = 'home.html'
    ctx['name'] = 'something cool'
    return render(request, tmt, ctx)
