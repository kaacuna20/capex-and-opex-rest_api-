from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tests.test_setup import TestSetup
from tests.factories.api_factories import CapexFactories, CapexRevenueFactory


class ApiCapexTestcase(TestSetup):
    
    def test_capex_list(self):
        capex_registered = CapexFactories().create_capex_transation()
        list_capex_url = reverse("capex")
        
        response = self.client.get(
            list_capex_url,
            {},
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_capex_df_per_month(self):
        capex_registered = CapexFactories().create_capex_transation()
        #capex_revenue = CapexRevenueFactory().create_capex_revenue()
        wrong_month = 15
        capex_df_url = f"/api/capex-df-month/1/{wrong_month}"
        
        response = self.client.get(
            capex_df_url,
            {},
            format='json'
        )
  
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"message": "DataFrame not found!"})
        
    def test_capex_df_per_year(self):
        capex_registered = CapexFactories().create_capex_transation()
        capex_revenue = CapexRevenueFactory().create_capex_revenue()
        wrong_year = 00000000
        capex_df_url = f"/api/capex-df-year/{wrong_year}"
        
        response = self.client.get(
            capex_df_url,
            {},
            format='json'
        )
  
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"message": "Bad request, make sure to write a right year format!"})
