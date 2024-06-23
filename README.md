<div class="row ">
	<div class="col ">
		<h1  style="color:#C6AB7C; font-size: 80px; font-weight:bold;">CapEx and OpEx Indicators in Maintenance</h1>
	</div>
</div>

<h4 align="justify">When I worked in VOPAK, my work team spent a lot of time copying data from erp system to google sheet and later create and/or update DashBoard about main KPI like Capex and Opex;
	and all that they did it manually, and I thought in a tool where could connect to <strong>erp database</strong>, get the the data of interest and plot in a customizing DashBoard automatically. Due to,
	I wanted to create an API where simulate this process in a minimalist way, users can register, login and feed to erp system and this, return <strong>dataframe in JSON format</strong> and with thoose dataframes, we could create a DashBoard in a dynamic way.
</h4> 

### Features of aplication

- Let login and logout creating routes for thoose actions;
- User can register and login session, access the routes where can interact with dataframes and fill the capex and opex data;
- Api must be documentated and show the routes where interact with methods and response to understand how api works;
- The method to authenticate users is JWT;
- Create and app where can render templates and show the api working with a minimalist dashboard;

## Table of Contents
- [Project Structure](#project-structure)
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [User Management Endpoints](#user-management-endpoints)
- [Data Visualization Endpoints](#data-visualization-endpoints)
- [Running the Project](#running-the-project)
- [Testing](#testing)
- [Running Tests](#running-tests)

## Project Structure
```ini
backend/
├── backend/
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
|   ├── settings.py
│   └── urls.py
│
├── api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
|   ├── serializers.py
|   ├── models.py
|   ├── urls.py
|   ├── views.py
|   └── migrations/
|
├── api_users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
|   ├── serializers.py
|   ├── models.py
|   ├── urls.py
|   ├── views.py
|   └── migrations/
|
├── data_visualization/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
|   ├── forms.py
|   ├── models.py
|   ├── test.py
|   ├── urls.py
|   ├── views.py
|   ├── migrations/
│   ├── templates/data_visualization/
│   │   ├── base.html
│   │   ├── chart.html
│   │   ├── index.html
│   │   └── login.html
|   └── static/data_visualization/
│       ├── base.css
│       └── image/
│
tests/
|    ├── factories/
|    ├── __init__.py
|    │   ├── __init__.py
|    │   ├── api_factories.py
|    │   └── api_user_factories.py
|    ├── test_api/
|    │   ├── __init__.py
|    │   ├── test_api_capex.py
|    │   └── test_api_opex.py
|    ├── test_api_user/
|    │   └── test_user.py
|    └── test_setup.py
|
├── venv/
├── db.sqlite3    
├── manage.py  
├── requirements.txt
└── .env

```

## Overview
This project consists of a Django application designed to manage CapEx (Capital Expenditure) and OpEx (Operating Expenditure) indicators in maintenance. The project is structured into three main apps:

1. `api`: Handles the creation, listing, and data retrieval of CapEx and OpEx transactions.
2. `api_users`: Manages user registration, authentication, and user-related operations.
3. `data_visualization`: Provides an interface to interact with the API and visualize the data using Plotly.

## Installation
1. Clone the repository:
   ```ini
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```
2. Create and activate a virtual environment:
    ```ini
    python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install the required packages:
    ```ini
    pip install -r requirements.txt
   ```
4. Apply the migrations:
    ```ini
    python manage.py migrate
    ```
5. Create a superuser:
   ```ini
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```ini
   python manage.py runserver
    ```
## Usage
### API Endpoints
CapEx Endpoints
- Create CapEx Transaction
  - URL: `/api/capex/create`
  - Method: POST
  - Permission: IsAuthenticated
  - Description: Create a new CapEx transaction.
  - Request Body:
    
       ```ini
        {
          "category": "Equipment",
          "description": "New machinery",
          "amount": 5000,
          "date": "2024-06-22"
        }
       ```
       
- List CapEx Transactions
  - URL: `/api/capex/`
  - Method: GET
  - Permission: IsAuthenticated
  - Description: List all CapEx transactions.
    
- Get CapEx DataFrame by Month
  - URL: `/api/capex-df-month/<year>/<month>/`
  - Method: GET
  - Permission: IsAuthenticated
  - Description: Retrieve a dataframe of CapEx transactions for a specific month.
    
- Get CapEx DataFrame by Year
  - URL: `/api/capex-df-year/<year>/`
  - Method: GET
  - Permission: IsAuthenticated
  - Description: Retrieve a dataframe of CapEx transactions for a specific year.

- Create CapEx Revenue
  - URL: `/api/capex-revenue/`
  - Method: POST
  - Permission: IsAuthenticated
  - Description: Create a new CapEx Revenue.
  - Request Body:
    
       ```ini
        {
          "revenue": 300000,
          "date": "2024-06-22"
        }
       ```
       
- List CapEx Revenue
  - URL: `/api/capex-revenue/`
  - Method: GET
  - Permission: IsAuthenticated
  - Description: List all CapEx Revenues.
    
OpEx Endpoints
- Create OpEx Transaction

  - URL: `/api/opex/create/`
  - Method: POST
  - Permission: IsAuthenticated
  - Description: Create a new OpEx transaction.
  - Request Body:
    ```ini
        {
          "category": "Utilities",
          "description": "Electricity bill",
          "amount": 200,
          "date": "2024-06-22"
        }
    ```
    
- List OpEx Transactions
  - URL: `/api/opex/`
  - Method: GET
  - Permission: IsAuthenticated
  - Description: List all OpEx transactions.
    
- Get OpEx DataFrame by Month
  - URL: `/api/opex-df-month/<year>/<month>/`
  - Method: GET
  - Permission: IsAuthenticated
  - Description: Retrieve a dataframe of OpEx transactions for a specific month.
    
- Get OpEx DataFrame by Year
  - URL: `/api/opex-df-year/<year>/`
  - Method: GET
  - Permission: IsAuthenticated
  - Description: Retrieve a dataframe of OpEx transactions for a specific year.

- Get CapEx and OpEx Percentage of Revenue
  - URL: `/api/opex-capex-revenue/<year>/`
  - Method: GET
  - Permission: IsAuthenticated
  - Description: Retrieve the percentage of revenue for CapEx and OpEx for a specific year.
 
- Create OpEx Revenue
  - URL: `/api/opex-revenue/create/`
  - Method: POST
  - Permission: IsAuthenticated
  - Description: Create a new OpEx Revenue.
  - Request Body:
    
       ```ini
        {
          "revenue": 300000,
          "date": "2024-06-22"
        }
       ```
       
- List OpEx Revenue
  - URL: `/api/opex-revenue/`
  - Method: GET
  - Permission: IsAuthenticated
  - Description: List all OpEx Revenues.

### User Management Endpoints
- Register User

  - URL: `/api-user/register/`
  - Method: POST
  - Permission: AllowAny
  - Description: Register a new user.
  - Request Body:
    ```ini
      {
        "username": "newuser",
        "password": "password123",
        "email": "user@example.com"
      }
    ```
    
- List Users
  - URL: `/api-user/list-users/`
  - Method: GET
  - Permission: IsAdminUser
  - Description: List all users (admin only).

- Change Password
  - URL: `/api-user/change-password/<int:id>/`
  - Method: PUT
  - Permission: IsAuthenticated
  - Description: Change the password for the authenticated user.
  - Request Body:
    ```ini
      {
        "password": "oldpassword123",
        "new_password": "newpassword123"
      }
    ```
  
- Desactivate User
  - URL: `/api-user/delete/<int:id>/`
  - Method: DELETE
  - Permission: IsAdminUser
  - Description: Deactivate a user (admin only).

- Login
  - URL: `/api-login/`
  - Method: POST
  - Permission: AllowAny
  - Description: Log in a user and obtain authentication tokens.
  - Request Body:
      ```ini
        {
          "username": "username",
          "password": "password123"
        }
     ```

- Logout
  - URL: `/api-logout/`
  - Method: POST
  - Permission: IsAuthenticated
  - Description: Log out a user and invalidate the authentication token.
      ```ini
      {
        "user": 1
      }
     ```
   
## Data Visualization Endpoints
- Index
  - URL: `/`
  - Method: GET
  - Description: Home page.

- Login Page
  - URL: `/login/`
  - Method: GET, POST
  - Description: Login page for users.

- Logout
  - URL: `/logout/`
  - Method: POST
  - Description: Logout the user.

- Chart Visualization
  - URL: `/chart/`
  - Method: GET
  - Description: Page to visualize CapEx and OpEx data using Plotly charts.

## Running the Project
To run the project, follow the steps in the Installation section. Ensure that you have applied the migrations and created a superuser. Then, run the development server using:
```ini
python manage.py runserver
```
You can access the API documentation generated by Swagger at:
```ini
http://127.0.0.1:8000/swagger/
```
## Testing
This project includes a comprehensive testing setup using Django's testing framework and the Django REST framework. The tests cover various aspects of the API, including user management, CAPEX, and OPEX transactions.

### Setting Up Tests
1. Create a `tests/ Directory`

Ensure that a tests/ directory exists at the same level as manage.py.

2. Create `test_setup.py`

This file contains the base setup for the tests, including user authentication.

   ```ini
	# tests/test_setup.py
	from django.urls import reverse
	from rest_framework import status
	from rest_framework.test import APITestCase
	from django.contrib.auth.models import User
	
	class TestSetup(APITestCase):
	    
	    def setUp(self):
	        self.user = User.objects.create_superuser(
	            username="test_username",
	            password='testpassword',
	            email="test@email.com"
	        )
	        
	        self.login_url = reverse("login")
	        
	        response = self.client.post(
	            self.login_url,
	            {
	                'username': "test_username",
	                'password': "testpassword"
	            },
	            format='json'
	        )
	        
	        self.assertEqual(response.status_code, status.HTTP_200_OK)
	        
	        self.token = response.data['token']
	       
	        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
	        return super().setUp()
   ```
3. Create factories/ Directory

This directory contains factory classes to create test data.
- api_factories.py

  ```ini
	  # tests/factories/api_factories.py
	from faker import Faker
	from django.contrib.auth.models import User
	import random
	from api.models import *
	
	faker = Faker()
	
	class CapexFactories:
	    
	    def create_capex_transation(self):
	        user = User.objects.create_user(
	            username="project_user",
	            password='project_user_password',
	            email=faker.email()
	        )
	        
	        contractor = CapexContractor.objects.create(
	            name=faker.company(),
	            nit=str(faker.random_number(digits=11))
	        )
	        
	        capex = CapexTransaction.objects.create(
	            date="2024-01-01",
	            description=faker.text(),
	            amount=15000, 
	            status=random.choice(STATUS_CHOICES),
	            category=random.choice(CAPEX_CHOICES),
	            contractor=contractor,
	            user_project=user
	        )
	        
	        return capex
	    
	class OpexFactories:
	    
	    def create_opex_transation(self):
	        user = User.objects.create_user(
	            username="planner_user",
	            password='planner_user_password',
	            email=faker.email()
	        )
	        
	        contractor = OpexContractor.objects.create(
	            name=faker.company(),
	            nit=str(faker.random_number(digits=11))
	        )
	        
	        opex = OpexTransaction.objects.create(
	            date="2024-01-01",
	            description=faker.text(),
	            amount=15000, 
	            status=random.choice(STATUS_CHOICES),
	            category=random.choice(OPEX_CHOICES),
	            contractor=contractor,
	            user_planner=user
	        )
	        
	        return opex
	    
	class CapexRevenueFactory:
	    def create_capex_revenue(self):
		capex_revenue = CapexRevenue.objects.create(
		revenue=300000,
		date="2024-01-01"
		)
		return capex_revenue
		
	class OpexRevenueFactory:
	    def create_opex_revenue(self):
		opex_revenue = OpexRevenue.objects.create(
		revenue=400000,
		date="2024-01-01"
		)
		return opex_revenue
	 ```
- api_user_factories.py
    ```ini
		# tests/factories/api_user_factories.py
	from faker import Faker
	from django.contrib.auth.models import User
	
	faker = Faker()
	
	class UserFactory:
	    
	    def create_user(self):
	        user = User.objects.create_user(
	            username="new_user",
	            password='new_password',
	            email=faker.email()
	        )
	        return user
	    
	    def user_desactivate(self):
	        user = User.objects.create_user(
	            username="new_user",
	            password='password',
	            email=faker.email(),
	            is_active=False
	        )
	        return user

	 ```
    
4. Create `test_api/` Directory
This directory contains test cases for the API endpoints.
- test_api_capex.py
  
	 ```ini
		# tests/test_api/test_api_capex.py
	from django.urls import reverse
	from rest_framework import status
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
	```
  
- test_api_opex.py
  
	 ```ini
		# tests/test_api/test_api_opex.py
	from django.urls import reverse
	from rest_framework import status
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
	
	```
  
5. Create `test_api_user/` Directory
This directory contains test cases for user-related API endpoints.
- test_user.py
  
	```ini
	# tests/test_api_user/test_user.py
	from django.urls import reverse
	from rest_framework import status
	from tests.test_setup import TestSetup
	from tests.factories.api_user_factories import UserFactory
	
	class ApiUserTestcase(TestSetup):
	    
	    def test_list_users(self):
	        user_registered = UserFactory().create_user()
	        list_users_url = reverse("list-users")
	        
	        response = self.client.get(
	            list_users_url,
	            {},
	            format='json'
	        )
	        
	        self.assertEqual(response.status_code, status.HTTP_200_OK)
	        self.assertEqual(len(response.data), 2)
	       
	    def test_change_password(self):
	        user_registered = UserFactory().create_user()
	        change_password_url = f"/api-user/change-password/{user_registered.pk}"
	        response = self.client.put(
	            change_password_url,
	            {"password": "new_password",
	             "new_password": "changed_password"
	            },
	            format='json'
	        )
	        self.assertEqual(response.status_code, status.HTTP_200_OK)
	        self.assertEqual(response.data, {'success': 'password changed successfully'})
	        
	    def test_delete_user(self):
	        user_registered = UserFactory().create_user()
	        delete_user_url = f"/api-user/delete/{user_registered.pk}"
	        response = self.client.delete(
	            delete_user_url,
	            {},
	            format='json'
	        )
	        
	        self.assertEqual(response.status_code, status.HTTP_200_OK)
	        self.assertEqual(response.data, {"message": "User has been desactivated sucessfully!"})
	        
	    def test_login(self):
	        user_desactivated = UserFactory().user_desactivate()
	        
	        login_url = reverse("login")
	        
	        response = self.client.post(
	            login_url,
	            {
	                'username': user_desactivated.username,
	                'password': "password"
	            },
	            format='json'
	        )
	        
	        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
	        self.assertEqual(response.data, {"error": "Password, Username wrong or User is invalid!"})
	
	
	```
 ## Running Tests
 To run the tests, execute the following command in your terminal:
 ```ini
	python manage.py test 
```
This command will discover and run all the test cases defined in the tests/ directory.

### Notes
- Ensure that the `django.urls` and `rest_framework` modules are installed and properly configured in your Django project.
- The `Faker` library is used for generating random test data. Make sure to install it via `pip install faker`.
- The `factories` module provides helper functions to create instances of your models for testing purposes.
- The `test_setup.py` file sets up the test environment, including creating a superuser and obtaining an authentication token for the tests.
- Test cases are organized into different files based on the functionality they cover, such as `test_api_capex.p`y for CAPEX-related tests, `test_api_opex.py` for OPEX-related tests, and `test_user.py` for user-related tests.
  
This setup ensures that your API is thoroughly tested and helps maintain the integrity of your application.
