from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from catalog.models import Product


class ProductList(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ProductDetails(DetailView):
    model = Product
    template = 'catalog/product_detail.html'


class ProductContact(TemplateView):
    model = Product
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'new message {name}({email}): {message}')
        return super().get_context_data(**kwargs)
