from django.db import IntegrityError
from django.db import transaction
from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated #widok tylko dla zalogowanych

from documents.api.permissions import IsAuthorOrReadOnly
from documents.api.serializers import AnswerSerializer, AnswerAssessmentSerializer, DocumentSerializer, DocumentAssessmentSerializer
from documents.models import Answer, AnswerAssessment, Document, DocumentAssessment


class DocumentViewSet(viewsets.ModelViewSet):
    """
    Widok do dodawania plików razem z metadanymi od użytkownika
    - pole document_code musi być unikalne i od razu podane [!]
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    #tylko autor który dodał plik może go usunąć/ zroibć update
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    #autoamtyczne dodawanie autora - nadpisanie wbudowanej metody
    def perform_create(self, serializer): # TODO: wycofywanie pliku tranzakcje gdy document_code nie jest unikalny
        serializer.save(author=self.request.user,
                document_file=self.request.data.get('document_file'))


class AnswerCreateAPIView(generics.CreateAPIView):
    """
    Umożliwia dodanie 
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # TODO: poprawić bledy z slug i id - nie mieszac ich
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        document = get_object_or_404(Document, id=int(kwarg_slug))

        serializer.save(author=request_user, document=document,
        answer_file=self.request.data.get('answer_file'))

class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Answer.objects.filter(document__slug=kwarg_slug).order_by("-created_at")

class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView): # RUD Retrieve Update Destroy
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]


############################ Ocenianie pojedynczego zadania przez użytkownika ############################
class AnswerAssessmentCreateAPIView(generics.CreateAPIView):
    """
    Umożliwia dodanie oceny do pojedynczego zadania
    """
    queryset = AnswerAssessment.objects.all()
    serializer_class = AnswerAssessmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_answer_id = self.kwargs.get("answerId")
        related_answer = get_object_or_404(Answer, id=int(kwarg_answer_id))

        serializer.save(author=request_user, answer=related_answer)

class AnswerAssessmentListAPIView(generics.ListAPIView):
    serializer_class = AnswerAssessmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_answer_id = self.kwargs.get("answerId")
        return AnswerAssessment.objects.filter(answer__id=kwarg_answer_id).order_by("-created_at")

class AnswerAssessmentRUDAPIView(generics.RetrieveUpdateDestroyAPIView): # RUD Retrieve Update Destroy
    queryset = AnswerAssessment.objects.all()
    serializer_class = AnswerAssessmentSerializer
    permission_classes = [IsAuthenticated]
