from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.http import FileResponse, Http404
from .forms import ProForm


# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})

def category_list(request):
    categories = Category.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)

    return render (request, 'blog/category_list.html', {'categories': categories}) # blog/category_list.html should be the template that categories are listed.

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)

    return render(request, 'blog/category_detail.html', {'category': category}) # in this template, you will have access to category and posts under that category by (category.post_set).


def new(request):
    return render(request, 'index.html')

def o_nas(request):
    return render(request, 'static/onas/index.html')
def pdf_view(request):
    try:
        return FileResponse(open('/static/pp.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def nowy_pro(request):
    form = ProForm()
    return render(request, 'nowy_produkt.html', {'form': form})