from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    task = TASK.objects.all()
    form  = TASKForm()



    if request .method =='POST':
        form = TASKForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    

    context = {'task': task, 'form': form}
    return render(request, 'task/list.html', context)



def updateTask(request, pk):   #pk means primary key
    assigned = TASK.objects.get(id = pk)
    
    form = TASKForm(instance = assigned)
    
    if request.method == 'POST':
        form = TASKForm(request.POST, instance = assigned)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'task/update_task.html', context)    


def deleteTask(request, pk):
    item  = TASK.objects.get(id = pk)


    if request.method =='POST':
        item.delete()
        return redirect('/')

        
    context = {'item':item}
    return render(request, "task/delete.html", context)    
