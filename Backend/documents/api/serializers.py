from rest_framework import serializers
from documents.models import Answer, AnswerAssessment, Document, DocumentAssessment

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    max_score =  serializers.SerializerMethodField()# maksymalna ilośc punktów za zadanie

    class Meta:
        model = Answer
        exclude = ["document", "updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y") # month day year

    def get_document_code(self, instance):
        """Zwraca unikalny kod znajdujący się na górze dokumentu"""
        return instance.document.document_code
    
    def get_document_file(self, instance):
        """Zwraca url do głównego dokumentu"""
        return instance.document.document_file.url

    def get_answer_file(self, instance):
        """Zwraca url do fragmentu pliku zadania z rozwiązaniem"""
        return instance.answer_file.get_file_url

    def get_max_score(self, instance):
        """Zwraca maksymalna liczbę punktów za zadanie"""
        return instance.max_score


class AnswerAssessmentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    scores =  serializers.SerializerMethodField() # liczba otrzymanych punktów

    class Meta:
        model = AnswerAssessment
        exclude = ["answer", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y") # month day year

    def get_answer(self, instance):
        """id zadania; Którego zadania to dotyczy"""
        return instance.answer.id

    def get_note(self, instance):
        """Zwraca notatkę do zadania"""
        return instance.note


class DocumentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    document_code = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Document
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y") # month day year

    def get_document_file(self, instance):
        """Zwraca url dokumentu"""
        return instance.document_file.url

    def get_document_code(self, instance):
        """Zwraca unikalny kod znajdujący się na górze dokumentu"""
        return instance.document_code


class DocumentAssessmentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    document_code = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = DocumentAssessment
        exclude = ["document", "updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y") # month day year
    
    def get_note(self, instance):
        """Zwraca notatkę do zadania"""
        return instance.note

    def get_document(self, instance):
        """Zwraca notatkę do zadania"""
        return instance.document.id
    
    def get_scores(self, instance):
        """Zwraca maksymalna liczbę punktów za zadanie"""
        return instance.scores
