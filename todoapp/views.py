from django.shortcuts import redirect, render

from todoapp.forms import TodoForm
from .models import Task
# Create your views here.


def home(request):
    show=Task.objects.all()
    if request.method == 'POST':
        task=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date')
        task=Task(name=task,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task':show})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method =='POST':
        task.delete()
        return redirect('/')

    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})
