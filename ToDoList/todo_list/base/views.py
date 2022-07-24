from operator import imod
from typing import Tuple
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView

from .models import task

'''
generic view will query the databse to get all records for
the specified model then render a template with .html file
where accesses by template variable name 'object_list', and shows all records.
'''
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    #redirect_authenticated_user to True to redirect users from the login page to the destination once the user is logged in.
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(ListView):
    #it will look for 'task_list.html'.
    model =  task
    #the default name of template variable is 'object_list'.
    #modifying it by using 'context_object_name'.
    context_object_name = 'tasks'
    
    # template file name can be changed by:
    # template_name = 'base/task.html'

class TaskDetail(DetailView):
    #it will look for 'task_detail.html'.
    model = task
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = task
    #that will pull out all fields in database.
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = task
    #
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')