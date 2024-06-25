from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("chart", views.chart, name="chart"),
    path("chart-month", views.chart_month, name="chart-month"),
    path("chart-year", views.chart_year, name="chart-year"),
    path("chart-revenue", views.chart_revenue, name="chart-revenue"),
    path("login", views.login, name="chart-login"),
    path("logout", views.logout, name="chart-logout"),
    
]