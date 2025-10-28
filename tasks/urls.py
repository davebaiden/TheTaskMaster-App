from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserTaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'user-tasks', UserTaskViewSet, basename='user-tasks')

urlpatterns = [
    path('', include(router.urls)),
]
