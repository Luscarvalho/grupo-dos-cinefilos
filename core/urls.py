from django.contrib import admin
from django.urls import path, include
from filmes import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FilmsHomeView.as_view(), name='home'),
    path('', include('usuario.urls')),
    path('filme/', include('filmes.urls')),
]
