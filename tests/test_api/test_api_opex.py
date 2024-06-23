from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tests.test_setup import TestSetup
from tests.factories.api_factories import OpexFactories, OpexRevenueFactory


class ApiOpexTestcase(TestSetup):
    
    def test_opex_list(self):
        opex_registered = OpexFactories().create_opex_transation()
        list_opex_url = reverse("opex")
        
        response = self.client.get(
            list_opex_url,
            {},
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_opex_df_per_month(self):
        opex_registered = OpexFactories().create_opex_transation()
     
        wrong_month = 15
        opex_df_url = f"/api/opex-df-month/1/{wrong_month}"
        
        response = self.client.get(
            opex_df_url,
            {},
            format='json'
        )
  
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"message": "DataFrame not found!"})
        
    def test_opex_df_per_year(self):
        opex_registered = OpexFactories().create_opex_transation()
        opex_revenue = OpexRevenueFactory().create_opex_revenue()
        wrong_year = 00000000
        opex_df_url = f"/api/opex-df-year/{wrong_year}"
        
        response = self.client.get(
            opex_df_url,
            {},
            format='json'
        )
  
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"message": "Bad request, make sure to write a right year format!"})