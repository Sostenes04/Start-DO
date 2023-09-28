from django.shortcuts import render
from django.views.generic import ListView
from .models import Tarefa

# Create your views here.

class Task(ListView):
    
    model = Tarefa
    template_name = 'Task/home.html'