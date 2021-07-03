from django.shortcuts import render
from store.models import Product
from django.views.generic import DetailView
# Create your views here.

def home(request):
	products = Product.objects.all().filter(is_available=True)
	context = {
		'products' : products
	}
	return render(request, 'home/home.html', context)

class ProductDetailView(DetailView):
	model = Product