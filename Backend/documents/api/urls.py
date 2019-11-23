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
    
    path("documents/answer/<int:id>/answerassessments/", 
        dv.AnswerAssessmentListAPIView.as_view(),
        name="answer-assessment"),

    path("documents/answer/<int:id>/answerassessment/", 
        dv.AnswerAssessmentCreateAPIView.as_view(),
        name="answer-assessment"),

    path("documents/<slug:slug>/answer/<int:id>/answerassessments/", 
        dv.AnswerAssessmentListAPIView.as_view(),
        name="answer-assessment"),

    path("documents/<slug:slug>/answer/<int:id>/answerassessment/", 
        dv.AnswerAssessmentCreateAPIView.as_view(),
        name="answer-assessment"),
]