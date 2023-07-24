from django.urls import path
from filmes import views

urlpatterns = [
    path('', views.FilmsListView.as_view(), name='films-list'),
    path('meus', views.MyFilmsListView.as_view(), name='my-films-list'),
    path('cadastrar/', views.FilmsCreateView.as_view(), name='films-create'),
    path('editar/<int:pk>',
         views.FilmsUpdateView.as_view(), name='films-update'),
    path('excluir/<int:pk>',
         views.FilmsDeleteView.as_view(), name='films-delete'),
    path('sortear/', views.FilmsSorteioView.sortear_filme,
         name='films-sort'),
    path('<int:pk>/',
         views.FilmsDetalhesView.as_view(), name='films-details'),
]
