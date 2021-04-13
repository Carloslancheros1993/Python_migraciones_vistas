from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter

from editoriales.views import EditorialViewSet

router = DefaultRouter()
router.register('', EditorialViewSet)

urlpatterns = router.urls