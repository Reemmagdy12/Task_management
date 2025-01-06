from django.urls import path
from .views import UserCreateView, TaskListCreateView, TaskDetailView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]