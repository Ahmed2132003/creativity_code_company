# portfolio/views.py
from django.shortcuts import render
from .models import PortfolioItem

def portfolio_view(request):
    portfolio_items = PortfolioItem.objects.all()  # جلب جميع العناصر من قاعدة البيانات
    return render(request, 'portfolio/portfolio.html', {'portfolio_items': portfolio_items})
