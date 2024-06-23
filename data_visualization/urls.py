from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("chart", views.chart, name="chart"),
    path("login", views.login, name="chart-login"),
    path("logout", views.logout, name="chart-logout"),
    
]