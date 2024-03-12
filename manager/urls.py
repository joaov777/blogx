
from . import views
from .views import login, home
from django.urls import path

urlpatterns = [
	path('login/', login, name="login"),
	path('', views.home, name="home"),
]