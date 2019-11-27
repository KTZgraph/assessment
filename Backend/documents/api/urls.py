from django.urls import include, path
from rest_framework.routers import DefaultRouter

from documents.api import views as dv

router = DefaultRouter()
router.register(r"documents", dv.DocumentViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path("document/<int:pk>/", 
        dv.DocumentRUDAPIView.as_view(),
        name="documentassessment-detail"),

    ######################## Documnet 1 <- N Answer ############################
    path("documents/<int:document_id>/answers/", 
        dv.AnswerListAPIView.as_view(),
        name="answer-list"),

    path("documents/<int:document_id>/answer/", 
        dv.AnswerCreateAPIView.as_view(),
        name="create-answer"),

    ######################## Documnet 1 <- N DocumentAssessment ############################
    path("documents/<int:document_id>/documentassessments/", 
        dv.DocumentAssessmentListAPIView.as_view(),
        name="documentassessment-list"),

    path("documents/<int:document_id>/documentassessment/", 
        dv.DocumentAssessmentCreateAPIView.as_view(),
        name="create-documentassessment"),

    path("documents/<int:document_id>/documentassessment/<int:pk>/", 
        dv.DocumentAssessmentRUDAPIView.as_view(),
        name="documentassessment-detail"),

    ######################## Documnet 1 <- N Answer ############################
    path("documents/<int:document_id>/answer/<int:pk>/", 
        dv.AnswerRUDAPIView.as_view(), 
        name="answer-detail"),

    path("answer/<int:pk>/",  #dla RUDAPI nazwa parametru musi być pk, inaczej 
        dv.AnswerRUDAPIView.as_view(), 
        name="answer-detail"),

    path("answer/<int:answer_id>/answerassessments/", 
        dv.AnswerAssessmentListAPIView.as_view(),
        name="answer-answerassessment-list"),

    path("answer/<int:answer_id>/answerassessment/", 
        dv.AnswerAssessmentCreateAPIView.as_view(),
        name="answer-create-answerassessment"),

    ######################## Answer 1 <- N AnswerAssessment ############################
    path("answer/<int:answer_id>/answerassessment/<int:pk>/", 
        dv.AnswerAssessmentRUDAPIView.as_view(), 
        name="answer-answerassessment-detail"),
    
    path("documents/<int:document_id>/answer/<int:answer_id>/answerassessment/", 
        dv.AnswerAssessmentCreateAPIView.as_view(),
        name="create-answerassessment"),

    path("documents/<int:document_id>/answer/<int:answer_id>/answerassessments/", 
        dv.AnswerAssessmentListAPIView.as_view(),
        name="answerassessment-list"),
    
    path("documents/<int:document_id>/answer/<int:answer_id>/answerassessment/<int:pk>/", 
        dv.AnswerAssessmentRUDAPIView.as_view(), 
        name="answerassessment-detail"),
]