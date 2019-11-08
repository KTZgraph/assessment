"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

#one_step views by ominąc weryfikacje emailową
from django_registration.backends.one_step.views import RegistrationView
from core.views import IndexTemplateView
from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # użycie wbudowanej rejestracji django ale z naszym skastomizowanym modelem
    path("accounts/register/", #custom version of the RegistrationView provided by django
        RegistrationView.as_view( # we used to create account bvia browser
            form_class=CustomUserForm,
            success_url="/",
        ), name="django_registration_register"),
    
    #reszta urli dostępna/wbudowana w django_registration
    path("accounts/", #other urls provided by django registration packets
        include("django_registration.backends.one_step.urls")),

    #logowanie przez przeglądarkę - standardowe dl aużytkownika
    path("accounts/", #login ursl provided by django
        include("django.contrib.auth.urls")),

    path("api/", #dodanie urli z api aplikacji users
        include("users.api.urls")),

    path("api-auth/", #login via browserable API
        include("rest_framework.urls")), #login users via browser
    
    path("api/rest-auth/", # login endpoint used via REST
        include("rest_auth.urls")),
    
    path("api/rest-auth/registration/", #registration endpoint to use via REST
        include("rest_auth.registration.urls")),
    
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]
