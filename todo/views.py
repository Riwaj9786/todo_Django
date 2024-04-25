from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Tasks


# Create your views here.


def todo(request):
    if request.method == 'POST':
        task = request.POST['task']
        desc = request.POST['desc']
        new_todo = Tasks(task = task, desc = desc)
        new_todo.save()


    tasks = Tasks.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'tasks': tasks,
    }
    # return redirect('/')
    return HttpResponse(template.render(context, request))


def delete(request, id):
    delete = Tasks.objects.get(id = id)
    delete.delete()
    return redirect('/')

def not_complete(request, id):
    item = Tasks.objects.get(id = id)
    item.status = False
    item.save()
    return redirect('/')

def complete(request, id):
    item = Tasks.objects.get(id = id)
    item.status = True
    item.save()
    return redirect('/')