from rest_framework import serializers
from users.models import CustomUser

# dla danych o zalogowanym aktualnie użytkowniku

class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username"]

