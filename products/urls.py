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
    url('cart/', views.cart, name='cart'),
]
