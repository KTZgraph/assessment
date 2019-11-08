from django.urls import include, path
from rest_framework.routers import DefaultRouter

from documents.api import views as dv

router = DefaultRouter()
router.register(r"documents", dv.DocumentViewSet)

urlpatterns = [
    path("", include(router.urls))
]