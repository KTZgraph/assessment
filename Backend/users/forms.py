from django_registration.forms import RegistrationForm
from users.models import CustomUser

class CustomUserForm(RegistrationForm):
    """Form dla rejestracji. By korzystać z wbudowanych dla django registration package ale z moim skastomizowanym 
    modelem użytkownika CustomUser"""

    class Meta(RegistrationForm.Meta):
        model = CustomUser