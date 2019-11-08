from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated #widok tylko dla zalogowanych

from documents.api.permissions import IsAuthorOrReadOnly
from documents.api.serializers import DocumentSerializer
from documents.models import Document


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    #tylko autor który dodał plik może go usunąć/ zroibć update
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    #autoamtyczne dodawanie autora - nadpisanie wbudowanej metody
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
