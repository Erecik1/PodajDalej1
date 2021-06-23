from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.http import FileResponse, Http404
from .forms import ProForm
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


# Create your views here.
"""def index(request):
    # return HttpResponse('Hello World')
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})
"""
def index(request):
    products = Product.objects.all()
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Product.objects.filter(name__contains=query_name)
            return render(request, 'index.html', {"results":results})

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

"""def nowy_pro(request):
    #POPRAWIĆ BO ZLE OZNACZENIA
    form = ProForm()
    if(request.method == 'POST'):
        name = request.POST['name']
        price = request.POST['price']
        stock = request.POST['stock']
        describe = request.POST['describe']
        category = Category.objects.get(id=request.POST['category'])
        image = request.FILES['image']
        action = Product(name = name, price = price, stock= stock, describe = describe,
        category = category, image = image)
        action.save()
        return redirect('home')
    return render(request, 'nowy_produkt.html', {'form': form})"""

def nowy_pro(request):
    if request.method == "POST":
        form = ProForm(request.POST, request.FILES)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.image = form.cleaned_data['image']
            newForm.save()
            return redirect('home')
    else:
        form = ProForm()
    return render(request, 'nowy_produkt.html', {'form': form})
        

def cart(request):
	return render(request, 'cart.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("index.html")
      
	form = ContactForm()
	return render(request, "contact.html", {'form':form})


def about(request):
    return render(request, 'about.html')

def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')