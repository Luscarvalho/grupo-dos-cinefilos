from .forms import CadastroForm
from django.views.generic import FormView
from django.urls import reverse_lazy


class CadastroView(FormView):
    template_name = 'cadastro.html'
    form_class = CadastroForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
