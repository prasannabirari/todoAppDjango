# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todos

# Create your views here.
def index(request):
    todos = Todos.objects.all()[:10]
    context = {
        'todos': todos
    }
    return render(request,'index.html',context)

def details(request,id):
    todo = Todos.objects.get(id=id)
    context = {
        'todo':todo
    }
    return render(request,'details.html',context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo = Todos(title=title, text=text)
        todo.save()
        return redirect('/todos')

    else:
        print "got get"
        return render(request,'add.html')
