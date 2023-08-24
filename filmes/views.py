import random
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from .forms import FilmsForm
from .models import Films


class FilmsHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'filmes/home.html'


class FilmsListView(LoginRequiredMixin, ListView):
    model = Films
    template_name = 'filmes/filmes.html'
    context_object_name = 'filme'


class MyFilmsListView(LoginRequiredMixin, ListView):
    model = Films
    template_name = 'filmes/meusfilmes.html'
    context_object_name = 'filme'

    def get_queryset(self):
        return Films.objects.filter(usuario=self.request.user)


class FilmsCreateView(LoginRequiredMixin, CreateView):
    model = Films
    form_class = FilmsForm
    template_name = 'filmes/form.html'
    success_url = reverse_lazy('my-films-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastrar Filme"
        context['botao'] = "Cadastrar"
        return context


class FilmsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Films
    template_name = 'filmes/form.html'
    fields = ['nome', 'ano']
    success_url = reverse_lazy('my-films-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Filme"
        context['botao'] = "Editar"
        return context

    def form_valid(self, form):
        film = self.get_object()
        if film.nome != form.cleaned_data['nome'] or film.ano != form.cleaned_data['ano']:
            existing_film = Films.objects.filter(nome=form.cleaned_data['nome'], ano=form.cleaned_data['ano']).exclude(
                pk=film.pk).first()
            if existing_film:
                form.add_error(
                    'nome', 'Um filme com o mesmo nome e ano já existe.')
                return self.form_invalid(form)
        if film.ano != form.cleaned_data['ano']:
            if not form.cleaned_data['ano'].isdigit():
                form.add_error('ano', 'O ano deve conter apenas números.')
                return self.form_invalid(form)
        return super().form_valid(form)

    def test_func(self):
        film = self.get_object()
        if self.request.user == film.usuario:
            return True
        else:
            messages.error(
                self.request, 'Você não tem permissão para editar este filme.')
            return False

    def handle_no_permission(self):
        return redirect('my-films-list')


class FilmsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Films
    template_name = 'filmes/delete.html'
    success_url = reverse_lazy('my-films-list')

    def test_func(self):
        film = self.get_object()
        if self.request.user == film.usuario:
            return True
        else:
            messages.error(
                self.request, 'Você não tem permissão para excluir este filme.')
            return False

    def handle_no_permission(self):
        return redirect('my-films-list')


class FilmsDetalhesView(LoginRequiredMixin, DetailView):
    model = Films
    template_name = 'filmes/detalhes.html'
    context_object_name = 'filme'


class FilmsSorteioView:
    def sortear_filme(self):
        films = Films.objects.all()
        films_nao_assistidos = Films.objects.filter(status=False)
        if not films_nao_assistidos and films:
            messages.error(self, 'Todos os filmes já vistos.')
            return redirect('films-list')
        elif not films_nao_assistidos and not films:
            messages.error(self, 'Nenhum filme cadastrado.')
            return redirect('films-list')
        else:
            filme_sorteado = random.choice(films_nao_assistidos)
            return redirect('films-details', filme_sorteado.pk)
