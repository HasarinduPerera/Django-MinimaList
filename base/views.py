from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    template_name = "base/task_list.html"
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    template_name = "base/task_detail.html"
    context_object_name = 'tasks'
