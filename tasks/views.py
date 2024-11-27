from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "tasks/tasks.html", {"tasks": tasks})


@login_required
def task_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST.get("description", "")
        Task.objects.create(user=request.user, title=title, description=description)
        return redirect("task-list")
    return render(request, "tasks/add_update_tasks.html")


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.title = request.POST["title"]
        task.description = request.POST.get("description", "")
        task.save()
        return redirect("task-list")
    return render(request, "tasks/add_update_tasks.html", {"task": task})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
    return redirect("task-list")
