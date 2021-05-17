from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import SignUpView
from . import views
from accounts.forms import LoginForm,SignUpForm
app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(),{'authentication_form':LoginForm}, name='login'),
    

]
