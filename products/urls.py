from django.urls import path
from django.conf.urls import include, url
from . import views


urlpatterns = [
    path('', views.index , name='home'),
    path('new/', views.new),
    path('about/',views.o_nas, name='onas'),
    path('nowy/', views.nowy_pro, name='new'),
    url(r'^category$', views.category_list, name='category_list'),
    url(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
    url('regulamin/', views.pdf_view),
    url('contact/', views.contact, name="contact"),
    url('cartview/', views.cart, name='cartview'),
    url('onas/', views.about, name='onas'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]
