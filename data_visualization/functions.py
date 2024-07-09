from django.http import JsonResponse
import plotly.express as px
import pandas as pd
import requests

def select_type_month(url_month:str, year:int, month:int, headers:dict, month_dict:dict, type:str):
    """
    Fetches data for a specific month and generates a histogram plot.

    Parameters:
    url_month (str): The base URL for the monthly data endpoint.
    year (int): The year of the data.
    month (int): The month of the data.
    headers (dict): The headers for the HTTP request.
    month_dict (dict): A dictionary mapping month numbers to month names.
    type (str): The type of data being requested (e.g., 'opex').

    Returns:
    str: An HTML string of the generated plot.
    """
    URL_TYPE_MONTH = f"{url_month}/{year}/{month}"
    
    response_opex_month = requests.get(url=URL_TYPE_MONTH , headers=headers)
    
    if response_opex_month.status_code == 401:
        return JsonResponse({"unauthorized": "Your session is over, please redirect to login again! "})
    
    if response_opex_month.status_code == 200:
    
        df_opex_month = pd.DataFrame(response_opex_month.json())
        
        fig = px.histogram(x=[c for c in df_opex_month["Description"]],
            y=[c for c in df_opex_month["Amount"]],
            title=f"{type.title()} {month_dict[int(month)]}",
            labels={'x': 'Description', 'y': 'Amount'})
        fig.update_layout(
                title={
                    'font_size': 24,
                    'xanchor': 'center',
                    'x': 0.5
            })
    else:
        fig = px.histogram(x=[0],
        y=[0],
        title=f"{type.title()} {month_dict[int(month)]}",
        labels={'x': 'Description', 'y': 'Amount'})
        fig.update_layout(
                title={
                    'font_size': 24,
                    'xanchor': 'center',
                    'x': 0.5
            })
    
    return fig.to_html()

def select_type_year(url_year:str, year:int, headers:dict, type:str):
    """
    Fetches data for a specific year and generates a line plot.

    Parameters:
    url_year (str): The base URL for the yearly data endpoint.
    year (int): The year of the data.
    headers (dict): The headers for the HTTP request.
    type (str): The type of data being requested (e.g., 'opex').

    Returns:
    str: An HTML string of the generated plot.
    """
    URL_TYPE_YEAR = f"{url_year}/{year}"
    
    response_opex_year = requests.get(url=URL_TYPE_YEAR, headers=headers)
    if response_opex_year.status_code != 200:
        return JsonResponse({"unauthorized": "Your session is over, please redirect to login again! "})
    df_opex_year = pd.DataFrame(response_opex_year.json())
    
    try:
        df_long = pd.melt(df_opex_year, id_vars=["Month"], value_vars=["Salaries", "Utilities", "Rent", "Operating Costs"],
                    var_name="Category", value_name="Amount")
    except KeyError:
        df_long = pd.melt(df_opex_year, id_vars=["Month"], value_vars=["Equipment", "Buildings", "Technology"],
                    var_name="Category", value_name="Amount")
    # Plot using plotly.express
    fig_1 = px.line(df_long, x="Month", y="Amount", color="Category", markers=True, title=f"{type.title()} {year}")

    # Add a title
    fig_1.update_layout(
            title={
                'font_size': 24,
                'xanchor': 'center',
                'x': 0.5
        })
    
    return fig_1.to_html()