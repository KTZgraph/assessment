from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify # typically this kind of strings are in urls

from core.utils import generate_random_string
from documents.models import Document

@receiver(pre_save, sender=Document) 
def add_slug_to_document(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.document_file.url)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string # manually assign slug + field before new instance is created
