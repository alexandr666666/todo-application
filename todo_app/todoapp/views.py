from django.shortcuts import render, redirect
from .forms import FormTask, FormSetting
from .models import Task

def open_main_page(request):
    task = Task.objects.all()
    return render(request, 'main-page.html', {'task': task})

def add_task(request):
    if request.method == 'POST':
        form = FormTask(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            time = form.cleaned_data['time']
            new_task = Task(text=text, time=time)
            new_task.save()
            return redirect('main-page')
    else:
        form = FormTask()
    return render(request, 'add-page.html', {'form': form})

def show_settings(request):
    form = FormSetting()
    return render(request, 'settings.html', {'form': form})