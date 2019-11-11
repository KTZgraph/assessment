from django.db import models
from django.conf import settings

def document_upload_to(instance, filename):
    return f'documents/{instance.document_code}/{filename}'

class Document(models.Model):
    """
    Model Plik dokumentu z zadaniami zawierajacy wiele odpowiedzi
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # TODO: wymusic na uzytkowniku unikalne id
    document_code = models.CharField(max_length=255) #, unique=True) # id dokumentu pobierane/uzupełniane ręcznie z góry pliku
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="documents")
     # file will be saved to MEDIA_ROOT/uploads/2015/01/30; albo zapisac pod document_code ?
    document_file = models.FileField(upload_to=document_upload_to, blank=True)
                                     #plik dokumentu zapisywany na dysku
    description = models.TextField(blank=True)
    scores = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return document_code # albo sćieżka do pliku self.document_file.url 


def answer_upload_to(instance, filename):
    return f'documents/{instance.document.document_code}/{filename}'


class Answer(models.Model):
    """
    Model zawierający fragmenty pliku będącego treścią zadania i rozwiązaniem 
    z pliku `class Document` z ocenami i uwagami nauczycieli 
    1 Dokument - N odpowiedzi
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # fragment pliku po wybraniu tresci zadania
    score =  models.PositiveSmallIntegerField() # liczba otrzymanych punktów
    max_score =  models.PositiveSmallIntegerField()# maksymalna ilośc punktów za zadanie
    note =  models.TextField(blank=True)# uwagi/notatka
    # autor dokumentu nie musi oceniać zadania
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    document = models.ForeignKey(Document,
                                    on_delete=models.CASCADE,
                                    related_name="answers")
    answer_file = models.FileField(upload_to=answer_upload_to, blank=True)


    def __str__(self):
        return self.author.username
