import os
import django

# Set the environment variable for Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Initialize Django
django.setup()

from django.db.models import Sum
from api.models import *
import pandas as pd
import matplotlib.pyplot as plt

c_rev = CapexRevenue.objects.values("revenue")
print([i["revenue"] for i in c_rev])

input_month = int(input())
input_year = int(input())

month_capex = CapexTransaction.objects.filter(date__month=input_month, date__year=input_year)

#print(CAPEX_CHOICES[0][0])

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
#print(month_capex_details)
#print(category)
#print(description)

print(sum(amount))

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

x_data = {}
list_months = []

#for month in month_dict:
    
    #list_months.append(month_dict[month])
x_data["Month"] = [month_dict[key] for key in month_dict]
for category in CAPEX_CHOICES:
    
    list_amount = []
    for month in month_dict:
       
        amount_filter = CapexTransaction.objects.filter(date__month=month, date__year=input_year, category=category[0])
        amount = [i["amount"] for i in amount_filter.values("amount")]
       
        
        list_amount.append(sum(amount))

    #
    x_data[category[1]] = list_amount

list_revenue = []
for month in month_dict:
    revenue_filter = CapexRevenue.objects.filter(date__month=month, date__year=input_year).values("revenue")
    revenue = [i["revenue"] for i in revenue_filter]
    list_revenue.append(sum(revenue))

x_data["Total Revenue"] = list_revenue
print(x_data)


# Detailed data for CapEx in January


#print(january_capex_details)
# Aggregated data for CapEx (January to March)
capex_data = {
    'Month': ['January', 'February', 'March'],
    'Equipment': [50000, 30000, 60000],
    'Buildings': [20000, 25000, 10000],
    'Technology': [10000, 15000, 20000],
    'Total Revenue': [300000, 300000, 300000]
}

#print(capex_data)

# Create DataFrames
month_capex_df = pd.DataFrame(month_capex_details)
#january_capex_df.to_json("january_capex.json", index=False)
capex_df = pd.DataFrame(capex_data)
#capex_df.to_json("capex.json", index=False)
print(month_capex_df)
print("#"*100)
print(capex_df)
print("#"*100)
category_capex = [category[1] for category in CAPEX_CHOICES] 
print(category_capex)
# Calculate Total CapEx and CapEx as a Percentage of Revenue
capex_df['Total CapEx'] = capex_df[category_capex].sum(axis=1)
capex_df['CapEx % of Revenue'] = (capex_df['Total CapEx'] / capex_df['Total Revenue']) * 100


# Plot CapEx
"""plt.figure(figsize=(12, 6))
plt.plot(capex_df['Month'], capex_df['Equipment'], label='Equipment', marker='o')
plt.plot(capex_df['Month'], capex_df['Buildings'], label='Buildings', marker='o')
plt.plot(capex_df['Month'], capex_df['Technology'], label='Technology', marker='o')
plt.plot(capex_df['Month'], capex_df['Total CapEx'], label='Total CapEx', marker='o', linestyle='--')
plt.title('Capital Expenditures (CapEx) Over Time')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('CapEx_Plot.png')
plt.show()"""

# Detailed data for OpEx in January

january_opex = OpexTransaction.objects.filter(date__month=1, date__year=2024)

category_filter = january_opex.values("category")
description_filter = january_opex.values("description")
amount_filter = january_opex.values("amount")
category = [i["category"] for i in category_filter]
description = [i["description"] for i in description_filter]
amount = [i["amount"] for i in amount_filter]
#print(category)
#print(description)
#print(sum(amount))

salaries_amount_filter = OpexTransaction.objects.filter(date__month=1, date__year=2024, category="salaries")
salaries_amount = [i["amount"] for i in salaries_amount_filter.values("amount")]
#print(sum(salaries_amount))

utilitie_amount_filter = OpexTransaction.objects.filter(date__month=1, date__year=2024, category="utilities")
utilitie_amount = [i["amount"] for i in utilitie_amount_filter.values("amount")]
#print(sum(utilitie_amount))

rent_amount_filter = OpexTransaction.objects.filter(date__month=1, date__year=2024, category="rent")
rent_amount = [i["amount"] for i in rent_amount_filter.values("amount")]
#print(sum(rent_amount))


january_opex_details = {
    'Category': category,
    'Description': description,
    'Amount': amount
}
#print(january_opex_details)

# Aggregated data for OpEx (January to March)
opex_data = {
    'Month': ['January', 'February', 'March'],
    'Salaries': [100000, 110000, 120000],
    'Utilities': [10000, 12000, 11000],
    'Rent': [5000, 5000, 5000],
    'Total Revenue': [300000, 300000, 300000]
}

#print(opex_data)

# Create DataFrames
january_opex_df = pd.DataFrame(january_opex_details)
#january_opex_df.to_json("january_opex.json", index=False)
opex_df = pd.DataFrame(opex_data)
#opex_df.to_json("opex.json", index=False)
print(january_opex_df)
print("#"*100)
print(opex_df)
print("#"*100)


category_opex = [category[1] for category in OPEX_CHOICES] 
print(category_opex)
# Calculate Total OpEx and OpEx as a Percentage of Revenue
opex_df['Total OpEx'] = opex_df[category_opex].sum(axis=1)
opex_df['OpEx % of Revenue'] = (opex_df['Total OpEx'] / opex_df['Total Revenue']) * 100

data = {
    'Month': capex_data["Month"],
    'Total CapEx': capex_df['Total CapEx'],
    'CapEx % of Revenue': capex_df['CapEx % of Revenue'],
    'Total OpEx': opex_df['Total OpEx'],
    'OpEx % of Revenue': opex_df['OpEx % of Revenue'] 
}
data_df = pd.DataFrame(data)
#data_df.to_json("kpi.json", index=False)
print(data_df)

# Plot OpEx
"""plt.figure(figsize=(12, 6))
plt.plot(opex_df['Month'], opex_df['Salaries'], label='Salaries', marker='o')
plt.plot(opex_df['Month'], opex_df['Utilities'], label='Utilities', marker='o')
plt.plot(opex_df['Month'], opex_df['Rent'], label='Rent', marker='o')
plt.plot(opex_df['Month'], opex_df['Total OpEx'], label='Total OpEx', marker='o', linestyle='--')
plt.title('Operational Expenditures (OpEx) Over Time')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('OpEx_Plot.png')
plt.show()"""

# Aggregating CapEx for January
"""january_capex = CapexTransaction.objects.filter(date__month=1, date__year=2024).aggregate(total_capex=Sum('amount'))
january_total_capex = january_capex['total_capex'] or 0

# Aggregating OpEx for January
january_opex = OpexTransaction.objects.filter(date__month=1, date__year=2024).aggregate(total_opex=Sum('amount'))
january_total_opex = january_opex['total_opex'] or 0

# Assuming total revenue for January is $300,000
total_revenue = 300000

# Calculating CapEx and OpEx as a percentage of revenue
capex_percentage_of_revenue = (january_total_capex / total_revenue) * 100
opex_percentage_of_revenue = (january_total_opex / total_revenue) * 100

print(f"January Total CapEx: ${january_total_capex:.2f}")
print(f"January CapEx as a Percentage of Revenue: {capex_percentage_of_revenue:.2f}%")
print(f"January Total OpEx: ${january_total_opex:.2f}")
print(f"January OpEx as a Percentage of Revenue: {opex_percentage_of_revenue:.2f}%")

# Create data for January
data = {
    'Month': ['January'],
    'Total CapEx': [january_total_capex],
    'CapEx % of Revenue': [capex_percentage_of_revenue],
    'Total OpEx': [january_total_opex],
    'OpEx % of Revenue': [opex_percentage_of_revenue]
}

# Create a DataFrame
df = pd.DataFrame(data)
#print(df)"""