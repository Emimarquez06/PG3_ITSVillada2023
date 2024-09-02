from django.urls import path
from .views import ComprarTelefonosUsadosView, SearchBrawlerView

urlpatterns = [
    path('comprar-telefonos-usados/', ComprarTelefonosUsadosView.as_view(), name='comprar_telefonos_usados'),
]

urlpatterns = [
    path('search/', SearchBrawlerView.as_view(), name='search_brawler'),  
]


