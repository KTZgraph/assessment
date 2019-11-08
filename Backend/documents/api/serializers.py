from rest_framework import serializers
from documents.models import Answer, Document

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    score =  serializers.SerializerMethodField() # liczba otrzymanych punktów
    max_score =  serializers.SerializerMethodField()# maksymalna ilośc punktów za zadanie
    note =  serializers.SerializerMethodField()# uwagi/notatka

    class Meta:
        model = Answer
        exclude = ["documents", "updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y") # month day year

    def get_document_code(self, instance):
        """Zwraca unikalny kod znajdujący się na górze dokumentu"""
        return instance.document.get_document_code
    
    def get_document_file(self, instance):
        """Zwraca url do głównego dokumentu"""
        return instance.document.document_file.url

    def get_answer_file(self, instance):
        """Zwraca url do fragmentu pliku zadania z rozwiązaniem"""
        return instance.answer_file.get_file_url


class DocumentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    document_code = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y") # month day year

    def get_document_file(self, instance):
        """Zwraca url dokumentu"""
        return instance.document_file.url
