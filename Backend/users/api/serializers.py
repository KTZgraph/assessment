from rest_framework import serializers
from users.models import CustomUser

# dla danych o zalogowanym aktualnie użytkowniku

class UserDisplaySerializer(serializers.ModelSerializer):
    """
    Dane te maja byc domyslnie dostępne tylko dla zalogowanych użytkowników
    dlatego w settings.py jest DEFAULT_PERMISSION_CLASSES
    """

    class Meta:
        model = CustomUser
        fields = ["username"]

