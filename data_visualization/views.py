from django.shortcuts import render
import requests
from .forms import DateForm
from django.http import JsonResponse
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
# Create your views here.


def chart(request):
    
    headers = {
        
        "Authorization": "Bearer JWT_LOGIN"
    }
    
    month_input = request.GET.get('month')
    year_input = request.GET.get('year')
    
    if month_input is None:
        month_input = 1
    if year_input is None:
        now = datetime.now()
        year_input = int(now.strftime("%Y"))
        
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
        
    
    URL_OPEX_MONTH = f"http://127.0.0.1:8000/api/opex-df-month/{year_input}/{month_input}"
    
    response_opex_month = requests.get(url=URL_OPEX_MONTH, headers=headers)
    df_opex_month = pd.DataFrame(response_opex_month.json())
    
    fig = px.histogram(x=[c for c in df_opex_month["Description"]],
        y=[c for c in df_opex_month["Amount"]],
        title=f"Opex {month_dict[int(month_input)]}",
        labels={'x': 'Description', 'y': 'Amount'})
    fig.update_layout(
            title={
                'font_size': 24,
                'xanchor': 'center',
                'x': 0.5
        })
    
    chart_opex_month = fig.to_html()
    
    URL_OPEX_YEAR = f"http://127.0.0.1:8000/api/opex-df-year/{year_input}"
    
    response_opex_year = requests.get(url=URL_OPEX_YEAR, headers=headers)
    df_opex_year = pd.DataFrame(response_opex_year.json())
    
    df_long = pd.melt(df_opex_year, id_vars=["Month"], value_vars=["Salaries", "Utilities", "Rent"],
                  var_name="Category", value_name="Amount")

    # Plot using plotly.express
    fig_1 = px.line(df_long, x="Month", y="Amount", color="Category", markers=True, title="Opex 2024")

    # Add a title
    fig_1.update_layout(
            title={
                'font_size': 24,
                'xanchor': 'center',
                'x': 0.5
        })
    
    chart_opex_year = fig_1.to_html()
    
    
    URL_OPEX_CAPEX_REVENUE = f"http://127.0.0.1:8000/api/opex-capex-revenue/{year_input}"
    
    response_revenue = requests.get(url=URL_OPEX_CAPEX_REVENUE, headers=headers)
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
    
    context = {'chart_opex_month': chart_opex_month,'chart_opex_year': chart_opex_year , 'chart_revenue': chart_revenue,'form': DateForm()}
    return render(request, 'data_visualization/chart.html', context)
    
    