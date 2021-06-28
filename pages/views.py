from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm


class HomePageView(TemplateView):
    template_name = "home.html"


def list_stocks(request):
    stocks = Stock.objects.all()
    return render(request, 'stock-list.html', {'stocks': stocks})  

def create_stock(request):
    form = StockForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pages:list_stocks')

    return render(request, 'stocks-form.html', {'form': form})  

def edit_stock(request, id):
    stock = Stock.objects.get(id=id)
    form = StockForm(request.POST or None, instance=stock)
    if form.is_valid():
        form.save()
        return redirect('pages:list_stocks')

    return render(request, 'stocks-form.html', {'form': form, 'stock': stock})  

def delete_stock(request, id):
    stock = Stock.objects.get(id=id)

    if request.method == 'POST':
        stock.delete()
        return redirect('pages:list_stocks')

    return render(request, 'stocks-delete-confirm.html', {'stocks': stock})  

