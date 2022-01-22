from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from .models import Task

# Create your views here.
class UserLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(ListView):
    model = Task
    template_name = "base/task_list.html"
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    template_name = "base/task_detail.html"
    context_object_name = 'tasks'

class TaskCreate(CreateView):
    model = Task
    template_name = "base/task_form.html"
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    #template_name = "base/update_form.html"
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
