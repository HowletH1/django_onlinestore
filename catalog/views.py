from django.shortcuts import render
from django.views.generic import DetailView
from catalog.models import Product


def home(request):
    objects_list = Product.objects.all()

    context = {
        'object_list': objects_list,
        'title': 'Интернет магазин'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'Имя: {name}, телефон: {phone};\n'
              f'Сообщение: {message}')
    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)


class ProductDetails(DetailView):
    model = Product
    template = 'catalog/product_detail.html'


def product(request, pk):

    context = {
        'object_list': Product.objects.get(pk=pk),
        'title': 'Страница товара'
    }

    return render(request, 'catalog/product_detail.html', context)
