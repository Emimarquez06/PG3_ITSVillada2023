from django.shortcuts import render
from django.views import View
from .utils import fetch_brawler_data
from django.views.generic import TemplateView

class ComprarTelefonosUsadosView(TemplateView):
    template_name = "brawlstars_app/new_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['extra_data'] = 'Este es un dato adicional que quiero pasar a la plantilla'
        
        return context

class SearchBrawlerView(View):
    template_name = 'brawlstars_app/search_brawler.html'
    result_template_name = 'brawlstars_app/brawler_info.html'

    def get(self, request):
        context = {
            'default_value': 'Este es un valor predeterminado'
        }
        return render(request, self.template_name, context)

    def post(self, request):
        brawler_name = request.POST.get('brawler_name')
        brawler_info = fetch_brawler_data(brawler_name)
        context = {'brawler_info': brawler_info}
        return render(request, self.result_template_name, context)
