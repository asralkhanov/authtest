from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register
from .import views

app_name = 'account'

urlpatterns = [
	path('', views.home, name='home'),
	path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
	path('register/',register, name='register'),
]