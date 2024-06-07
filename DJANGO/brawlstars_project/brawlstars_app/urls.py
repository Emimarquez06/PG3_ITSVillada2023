from django.urls import path
from .views import search_brawler

app_name = 'brawlstars_app'

urlpatterns = [
    path('search/', search_brawler, name='search_brawler'),
]
