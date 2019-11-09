from django.apps import AppConfig


class DocumentsConfig(AppConfig):
    name = 'documents'

    # signals
    def ready(self):
        import documents.signals # after this change __init__.py
