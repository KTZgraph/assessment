from django.db import IntegrityError
from django.db import transaction
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated #widok tylko dla zalogowanych

from documents.api.permissions import IsAuthorOrReadOnly
from documents.api.serializers import DocumentSerializer
from documents.models import Document


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
    def perform_create(self, serializer): # TODO: wycofywanie pliku tranzakcje
        try:
            serializer.save(author=self.request.user,
                            document_file=self.request.data.get('document_file'))
        except BaseException as ex:
            import traceback; traceback.print_exc()
            print("EEEEEEEEEEEEEEEEEEEEEEEEEE: ", ex)
        

            
    
