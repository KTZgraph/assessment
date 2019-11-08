from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    """
    Dziedziczenie po LoginRequiredMixin - 
    widok ma być dostępny tylko dla zalogowanych/autoryzowanych użytkowników
    """

    def get_template_names(self):
        template_name = "index.html"
        return template_name