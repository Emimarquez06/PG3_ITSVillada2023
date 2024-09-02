from django.contrib import admin
from django.urls import path, include
from brawlstars_app.views import ComprarTelefonosUsadosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ComprarTelefonosUsadosView.as_view(), name='home'),  
    path('brawlstars/', include('brawlstars_app.urls')),
]
