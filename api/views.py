from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
import numpy as np


# Create your views here.

# OPEX AND CAPEX VIEWS
class CreateCapexView(generics.CreateAPIView):
    queryset = CapexTransaction.objects.all()
    serializer_class = CapexTransactionSerializer
    permission_classes = [IsAuthenticated]


class CreateOpexView(generics.CreateAPIView):
    queryset = OpexTransaction.objects.all()
    serializer_class = OpexTransactionSerializer
    permission_classes = [IsAuthenticated]


class ListCapexView(generics.ListAPIView):
    serializer_class = CapexTransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return CapexTransaction.objects.all()
    
    
class ListOpexView(generics.ListAPIView):
    serializer_class = OpexTransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return OpexTransaction.objects.all()


class CreateCapexRevenueView(generics.CreateAPIView):
    queryset = CapexRevenue.objects.all()
    serializer_class = CapexRevenueSerializers
    permission_classes = [IsAuthenticated]


class CreateOpexRevenueView(generics.CreateAPIView):
    queryset = OpexRevenue.objects.all()
    serializer_class = OpexRevenueSerializers
    permission_classes = [IsAuthenticated]


class ListCapexRevenueView(generics.ListAPIView):
    serializer_class = CapexRevenueSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return CapexRevenue.objects.all()
    
    
class ListOpexRevenueView(generics.ListAPIView):
    serializer_class = OpexRevenueSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return OpexRevenue.objects.all()


# OPEX AND CAPEX DATAFRAME VIEWS

class CapexDataFramePerMonth(APIView):

    serializer_class = CapexTransactionSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, year, month):
        """
        Return a dataframe from capex in that month and year.
        """
        
        month_capex = CapexTransaction.objects.filter(date__month=month, date__year=year)
        if month_capex:
            category_filter = month_capex.values("category")
            description_filter = month_capex.values("description")
            amount_filter = month_capex.values("amount")
            category = [i["category"] for i in category_filter]
            description = [i["description"] for i in description_filter]
            amount = [i["amount"] for i in amount_filter]
            
            
            month_capex_details = {
            'Category': category,
            'Description': description,
            'Amount': amount
            }
        
            return Response(month_capex_details, status=status.HTTP_200_OK)
        return Response({"message": "DataFrame not found!"}, status=status.HTTP_404_NOT_FOUND)

    
class OpexDataFramePerMonth(APIView):

    serializer_class = OpexTransactionSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, year, month):
        """
        Return a dataframe from opex in that month and year.
        """
        month_capex = OpexTransaction.objects.filter(date__month=month, date__year=year)
        if month_capex:
            category_filter = month_capex.values("category")
            description_filter = month_capex.values("description")
            amount_filter = month_capex.values("amount")
            category = [i["category"] for i in category_filter]
            description = [i["description"] for i in description_filter]                
            amount = [i["amount"] for i in amount_filter]
                
                
            month_capex_details = {
                'Category': category,
                'Description': description,
                'Amount': amount
            }
            
            return Response(month_capex_details, status=status.HTTP_200_OK)
        return Response({"message": "DataFrame not found!"}, status=status.HTTP_404_NOT_FOUND)
  
    
class CapexDataFramePerYear(APIView):
    serializer_class = CapexTransactionSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, year):
        """
        Return a dataframe from capex per year.
        """
        month_dict = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }

        capex_data = {}
        capex_data["Month"] = [month_dict[key] for key in month_dict]
        try:
            for category in CAPEX_CHOICES:
        
                list_amount = []
                for month in month_dict:
                
                    amount_filter = CapexTransaction.objects.filter(date__month=month, date__year=year, category=category[0])
                    amount = [i["amount"] for i in amount_filter.values("amount")]
            
                    list_amount.append(sum(amount))
                    
                capex_data[category[1]] = list_amount
            
            list_revenue = []
            for month in month_dict:
                revenue_filter = CapexRevenue.objects.filter(date__month=month, date__year=year).values("revenue")
                revenue = [i["revenue"] for i in revenue_filter]
                list_revenue.append(sum(revenue))

            capex_data["Total Revenue"] = list_revenue
                
            return Response(capex_data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"message": "Bad request, make sure to write a right year format!"}, status=status.HTTP_400_BAD_REQUEST)


class OpexDataFramePerYear(APIView):
    serializer_class = OpexTransactionSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, year):
        """
        Return a dataframe from opex per year.
        """
        month_dict = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }

        opex_data = {}
        opex_data["Month"] = [month_dict[key] for key in month_dict]
        try:
            for category in OPEX_CHOICES:
        
                list_amount = []
                for month in month_dict:
                
                    amount_filter = OpexTransaction.objects.filter(date__month=month, date__year=year, category=category[0])
                    amount = [i["amount"] for i in amount_filter.values("amount")]
            
                    list_amount.append(sum(amount))
                    
                opex_data[category[1]] = list_amount
            
            list_revenue = []
            for month in month_dict:
                revenue_filter = OpexRevenue.objects.filter(date__month=month, date__year=year).values("revenue")
                revenue = [i["revenue"] for i in revenue_filter]
                list_revenue.append(sum(revenue))

            opex_data["Total Revenue"] = list_revenue
                
            return Response(opex_data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"message": "Bad request, make sure to write a right year format!"}, status=status.HTTP_400_BAD_REQUEST)
    
        
class CapexOpexPercentageRevenue(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, year):
        """
        Return a dataframe from capex and opex in percentage of revenue per year.
        """
        month_dict = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }

        try:
            opex_data = {}
            opex_data["Month"] = [month_dict[key] for key in month_dict]
            
            for category in OPEX_CHOICES:
                
                list_amount = []
                for month in month_dict:
                        
                    amount_filter = OpexTransaction.objects.filter(date__month=month, date__year=year, category=category[0])
                    amount = [i["amount"] for i in amount_filter.values("amount")]
                    
                    list_amount.append(sum(amount))
                            
                opex_data[category[1]] = list_amount
                    
            list_revenue = []
            for month in month_dict:
                revenue_filter = OpexRevenue.objects.filter(date__month=month, date__year=year).values("revenue")
                revenue = [i["revenue"] for i in revenue_filter]
                list_revenue.append(sum(revenue))

            opex_data["Total Revenue"] = list_revenue
            opex_df = pd.DataFrame(opex_data)
            category_opex = [category[1] for category in OPEX_CHOICES] 
        
            # Ensure numeric columns are of type float
            opex_df['Total Revenue'] = opex_df['Total Revenue'].astype(float)
            for col in category_opex:
                opex_df[col] = opex_df[col].astype(float)

            opex_df['Total OpEx'] = opex_df[category_opex].sum(axis=1)

            # Calculate OpEx % of Revenue with zero division handling
            opex_df['OpEx % of Revenue'] = np.where(
                opex_df['Total Revenue'] != 0, 
                (opex_df['Total OpEx'] / opex_df['Total Revenue']) * 100, 
                0
            )
                
            capex_data = {}
            capex_data["Month"] = [month_dict[key] for key in month_dict]
                
            for category in CAPEX_CHOICES:
                
                list_amount = []
                for month in month_dict:
                        
                    amount_filter = CapexTransaction.objects.filter(date__month=month, date__year=year, category=category[0])
                    amount = [i["amount"] for i in amount_filter.values("amount")]
                    
                    list_amount.append(sum(amount))
                            
                capex_data[category[1]] = list_amount
                    
            list_revenue = []
            for month in month_dict:
                revenue_filter = CapexRevenue.objects.filter(date__month=month, date__year=year).values("revenue")
                revenue = [i["revenue"] for i in revenue_filter]
                list_revenue.append(sum(revenue))

            capex_data["Total Revenue"] = list_revenue
            capex_df = pd.DataFrame(capex_data)
            category_capex = [category[1] for category in CAPEX_CHOICES]
             
            # Ensure numeric columns are of type float
            capex_df['Total Revenue'] = capex_df['Total Revenue'].astype(float)
            for col in category_capex:
                capex_df[col] = capex_df[col].astype(float)

        
            capex_df['Total CapEx'] = capex_df[category_capex].sum(axis=1)

            # Calculate CapEx % of Revenue with zero division handling
            capex_df['CapEx % of Revenue'] = np.where(
                capex_df['Total Revenue'] != 0, 
                (capex_df['Total CapEx'] / capex_df['Total Revenue']) * 100, 
                0
            )
                
            data = {
                    'Month': capex_data["Month"],
                    'Total CapEx': capex_df['Total CapEx'],
                    'CapEx % of Revenue': capex_df['CapEx % of Revenue'],
                    'Total OpEx': opex_df['Total OpEx'],
                    'OpEx % of Revenue': opex_df['OpEx % of Revenue'] 
            }
        
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"message": "Bad request, make sure to write a right year format!"}, status=status.HTTP_400_BAD_REQUEST)

