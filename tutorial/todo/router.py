from rest_framework.routers import DefaultRouter
from .views import StatusViewSet, TaskViewSet

router = DefaultRouter()

router.register(r'statuses', StatusViewSet)
router.register(r'tasks', TaskViewSet)