from django.urls import path
from . import views

urlpatterns = [

    path("capex/create", views.CreateCapexView.as_view(), name="create-capex"),
    path("opex/create", views.CreateOpexView.as_view(), name="create-opex"),
    path("capex", views.ListCapexView.as_view(), name="capex"),
    path("opex", views.ListOpexView.as_view(), name="opex"),
    
    path("capex-revenue/create", views.CreateCapexRevenueView.as_view(), name="create-capex-revenue"),
    path("opex-revenue/create", views.CreateOpexRevenueView.as_view(), name="create-opex-revenue"),
    path("capex-revenue", views.ListCapexRevenueView.as_view(), name="capex-revenue"),
    path("opex-revenue", views.ListOpexRevenueView.as_view(), name="opex-revenue"),
    
    path("capex-df-month/<int:year>/<int:month>", views.CapexDataFramePerMonth.as_view(), name="capex-df-month"),
    path("opex-df-month/<int:year>/<int:month>", views.OpexDataFramePerMonth.as_view(), name="opex-df-month"),
    path("capex-df-year/<int:year>", views.CapexDataFramePerYear.as_view(), name="capex-df-year"),
    path("opex-df-year/<int:year>", views.OpexDataFramePerYear.as_view(), name="opex-df-year"),
    path("opex-capex-revenue/<int:year>", views.CapexOpexPercentageRevenue.as_view(), name="capex-opex-percentage-revenue"),
  
]