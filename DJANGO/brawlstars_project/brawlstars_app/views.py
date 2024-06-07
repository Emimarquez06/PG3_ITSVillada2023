from django.shortcuts import render
from .utils import fetch_brawler_data

def search_brawler(request):
    if request.method == 'POST':
        brawler_name = request.POST.get('brawler_name')
        brawler_info = fetch_brawler_data(brawler_name)
        return render(request, 'brawler_info.html', {'brawler_info': brawler_info})
    return render(request, 'search_brawler.html')
