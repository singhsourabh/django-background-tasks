from django.shortcuts import render
from django.http import HttpResponse
from task.tasks import add_todo
from .models import Todo

def index(request):
    add_todo(10)
    query = Todo.objects.all()
    return HttpResponse(query)