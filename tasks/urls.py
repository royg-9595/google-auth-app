from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("task/add/", views.task_create, name="task-create"),
    path("task/<int:pk>/edit/", views.task_edit, name="task-edit"),
    path("task/<int:pk>/delete/", views.task_delete, name="task-delete"),
]
