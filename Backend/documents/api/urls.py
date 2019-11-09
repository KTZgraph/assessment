from django.urls import include, path
from rest_framework.routers import DefaultRouter

from documents.api import views as dv

router = DefaultRouter()
router.register(r"documents", dv.DocumentViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path("documents/<slug:slug>/answers/", 
        dv.AnswerListAPIView.as_view(),
        name="answer-list"),

    path("documents/<slug:slug>/answer/", 
        dv.AnswerCreateAPIView.as_view(),
        name="create-answer"),
    
    # path("documents/<int:id>/answer/", 
    #     dv.AnswerCreateAPIView.as_view(),
    #     name="id-create-answer")
]