from django.shortcuts import render
import requests
from .forms import DateForm, LoginForm
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os
from data_visualization.functions import select_type_month, select_type_year

load_dotenv(".env")
# Create your views here.


def index(request):
    return render(request, "data_visualization/index.html")

def login(request):
    login_form = LoginForm()
    url = os.getenv('MAIN_URL')
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        
        if login_form.is_valid():
            user = request.POST["username"]
            password = request.POST["password"]
        
            parameters = {
                "username": user,
                "password": password
            }
         
            response = requests.post(url=f"{url}/api-login/", json=parameters)
            
            if response.status_code == 200:
                request.session["token"] = response.json()["token"]
                request.session["user"] = response.json()["user"]['id']
                return HttpResponseRedirect("/chart")
            else:
                return JsonResponse(response.json())
    
    return render(request, 'data_visualization/login.html', context={
        "form": login_form
    })
    
def logout(request):
    url = os.getenv('MAIN_URL')
    if request.method == "POST":
        user_id = request.session.get("user")
        access_token = request.session.get("token")
        
        headers = {
            "Authorization": access_token
        }
        
        parameters = {
                    "user": user_id,
                }
        response = requests.post(url=f"{url}/api-logout/", json=parameters, headers=headers)
        if response.status_code == 200:
            request.session["token"] = None
            request.session["user"] = None
            return HttpResponseRedirect("/login")
        return JsonResponse({"unauthorized": "You haven't Logged in, redirect to login session! "})

def chart(request):
    access_token = request.session.get("token")
    if access_token is None:
        return JsonResponse({"unauthorized": "You haven't Logged in, redirect to login session! "})
    
    return render(request, 'data_visualization/chart.html')
    
    
def chart_month(request): 
    access_token = request.session.get("token")
    if access_token is None:
        return JsonResponse({"unauthorized": "You haven't Logged in, redirect to login session! "})
    
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
    
    headers = {
        "Authorization": access_token
    }
    
    month_input = request.GET.get('month')
    year_input = request.GET.get('year')
    type_input = request.GET.get('type')
    
    if month_input is None:
        month_input = 1
        
    if year_input is None:
        now = datetime.now()
        year_input = int(now.strftime("%Y"))
    
    url = os.getenv('MAIN_URL')
    
    if type_input is None:
        type_input = "capex"
        
    if type_input == "capex":
        url_month = f"{url}/api/capex-df-month"
       
    elif type_input == "opex":
        url_month = f"{url}/api/opex-df-month"
    
    chart_type_month = select_type_month(url_month, int(year_input), int(month_input), headers, month_dict, type_input)
    
    context = {'chart_type_month': chart_type_month,'form': DateForm(), "title":type_input}
    
    return render(request, 'data_visualization/month_chart.html', context)

def chart_year(request):
    access_token = request.session.get("token")
    if access_token is None:
        return JsonResponse({"unauthorized": "You haven't Logged in, redirect to login session! "})
              
    headers = {
        "Authorization": access_token
    }
        
    year_input = request.GET.get('year')
    type_input = request.GET.get('type')
            
    if year_input is None:
        now = datetime.now()
        year_input = int(now.strftime("%Y"))
        
    url = os.getenv('MAIN_URL')
        
    if type_input is None:
        type_input = "capex"
            
    if type_input == "capex":
        url_year = f"{url}/api/capex-df-year"
   
    elif type_input == "opex":
        url_year = f"{url}/api/opex-df-year"
        
    chart_type_year = select_type_year(url_year, int(year_input), headers, type_input)        
    context = {'chart_type_year': chart_type_year, 'form': DateForm(), "title":type_input}
        
    return render(request, 'data_visualization/year_chart.html', context)
        
    
def chart_revenue(request):
    access_token = request.session.get("token")
    if access_token is None:
        return JsonResponse({"unauthorized": "You haven't Logged in, redirect to login session! "})
              
    headers = {
        "Authorization": access_token
    }
        
    year_input = request.GET.get('year')
   
        
    if year_input is None:
        now = datetime.now()
        year_input = int(now.strftime("%Y"))
        
    url = os.getenv('MAIN_URL')
    URL_OPEX_CAPEX_REVENUE = f"{url}/api/opex-capex-revenue/{year_input}"
    
    response_revenue = requests.get(url=URL_OPEX_CAPEX_REVENUE, headers=headers)
    
    if response_revenue.status_code != 200:
        return JsonResponse({"unauthorized": "Your session is over, please redirect to login again! "})
    
    df_revenue = pd.DataFrame(response_revenue.json())
    
    fig_2 = go.Figure()

    # Add traces for percentages
    fig_2.add_trace(go.Scatter(x=df_revenue['Month'], y=df_revenue['CapEx % of Revenue'], mode='lines+markers', name='CapEx % of Revenue', yaxis='y1'))
    fig_2.add_trace(go.Scatter(x=df_revenue['Month'], y=df_revenue['OpEx % of Revenue'], mode='lines+markers', name='OpEx % of Revenue', yaxis='y1'))

    # Add traces for totals
    fig_2.add_trace(go.Bar(x=df_revenue['Month'], y=df_revenue['Total CapEx'], name='Total CapEx', yaxis='y2', opacity=0.6))
    fig_2.add_trace(go.Bar(x=df_revenue['Month'], y=df_revenue['Total OpEx'], name='Total OpEx', yaxis='y2', opacity=0.6))

    # Update layout for dual y-axes
    fig_2.update_layout(
        title='CapEx and OpEx: Percentage of Revenue and Total Values',
        xaxis=dict(title='Month'),
        yaxis=dict(
            title='Percentage of Revenue',
            titlefont=dict(color='#1f77b4'),
            tickfont=dict(color='#1f77b4'),
            side='left'
        ),
        yaxis2=dict(
            title='Total Values',
            titlefont=dict(color='#ff7f0e'),
            tickfont=dict(color='#ff7f0e'),
            overlaying='y',
            side='right'
        ),
        legend=dict(x=0.1, y=1.1, orientation='h'),
        margin=dict(l=40, r=40, t=80, b=40)
    )
    chart_revenue = fig_2.to_html()
    
    context = {'chart_revenue': chart_revenue,'form': DateForm()}
    return render(request, 'data_visualization/revenue_chart.html', context)
    
    