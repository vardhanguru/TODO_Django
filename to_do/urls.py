from django.urls import path 
from . import views

urlpatterns=[
    path('',views.todoHome,name='todo-home'),
    path('/task',views.taskList,name='taskList'),
    path('/tasks',views.allTasks,name='all-tasks'),
    path('/task-completed',views.taskcompleted,name='task-completed'),
    path('/task-delete',views.taskdelete,name='task-delete'),
    path('/task-edit',views.taskedit,name='task-edit'),

]