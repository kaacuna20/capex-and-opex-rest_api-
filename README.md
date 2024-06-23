<div class="row ">
	<div class="col ">
		<h1  style="color:#C6AB7C; font-size: 80px; font-weight:bold;">CapEx and OpEx Indicators in Maintenance</h1>
	</div>
</div>

<h4 align="justify">In the Atlantico department - Colombia, there are many housing projects, of many types (VIS, VIP, NO VIS) where people of all classes can get their own home, but there are many options and I thought the following, why not create a website where people can search all options in one site instead to do it website by website? I decided start to create my first big project, using my knowlegde of HTML, CSS, Bootstrap, Python and two of its frameworks, FastApi and Flask and last, conect all this using docker containers.</h4> 

### Features of aplication

- Let view housing projects in Atlantico - Colombia, specifically in Puerto Colombia, Barranquilla and Soledad city, filter the search by construction company, location and city;
- User can register and login section, personalize their profiles and save their favorites projects on their accounts;
- got the option to change their passwords or get a new password in section forgot password where the new password is sent to their email;
- Each project page there is a comment section where each user can leave their opinions about the project;
- There is a section for developer where can read the documentation about the API, whatching the routes to make the requests, the differents responses and restrictions;
- Developers can generate their apikey to be allowed making requests;

## Table of Contents
- [Project Structure](#Project-Structure)
- [Overview](#overview)
- [Installation](#Installation)
- [Usage](#Usage)
- [API Endpoints](#API-Endpoints)
- [User Management Endpoints](#User-Management-Endpoints)
- [Data Visualization Endpoints](#Data-Visualization-Endpoints)
- [Running the Project](#Running-the-Project)

## Project Structure
```ini
Website-house-project-searching/
├── images/
│   ├── api/
│   └── profile/
├── postgresql_db/
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
├── api-house-finder/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── run.py
│   └── app/
│      ├── __init__.py
│      ├── database.py
│      ├── main.py
│      ├── models.py
│      ├── helper/
│      │     ├── download_img.py
│      │     └── normalize_text.py
│      ├── routers/	
│      │  ├── __init__.py
│      │  └── projects.py
│      ├── utils/	
│      │  ├── __init__.py
│      │  └── auth.py
│      └── test_project.py
│
├── webapp-house-finder/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── run.py
|   ├── config.py
│   └── app/
│      ├── __init__.py
│      ├── models.py
│      ├── auth/
│      │     ├── __init__.py
│      │     └── forms.py
|      ├── common/
│      │     ├── __init__.py
│      │     └── mail.py
│      ├── routers/	
│      │   ├── __init__.py
|      │   ├── api_documentation.py
|      │   ├── api.py
|      │   ├── index.py
|      │   ├── profile.py
|      │   ├── user.py
│      │   └── project.py
|      ├── templates/
|      ├── static/
│      ├── utils/	
│      │  ├── __init__.py
│      │  └── helpers.py
│      └── test/
|         ├── __init__.py
|         ├── conftest.py
|         ├── test_api_route.py
|         ├── test_profile_route.py
|         └── test_user_route.py
│   
├── docker-compose.png  
├── docker-compose.yml
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
  - URL: /api/capex/
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
  - URL: /api/capex/
  - Method: GET
  - Permission: IsAuthenticated
  - Description: List all CapEx transactions.
    
- Get CapEx DataFrame by Month
  - URL: /api/capex-df-month/<year>/<month>/
  - Method: GET
  - Permission: IsAuthenticated
  - Description: Retrieve a dataframe of CapEx transactions for a specific month.
    
- Get CapEx DataFrame by Year
  - URL: /api/capex-df-year/<year>/
  - Method: GET
  - Permission: IsAuthenticated
  - Description: Retrieve a dataframe of CapEx transactions for a specific year.

OpEx Endpoints
- Create OpEx Transaction

  - URL: /api/opex/
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
  - URL: /api/opex/
  - Method: GET
  - Permission: IsAuthenticated
  - Description: List all OpEx transactions.
    
- Get OpEx DataFrame by Month
  - URL: /api/opex-df-month/<year>/<month>/
  - Method: GET
  - Permission: IsAuthenticated
  - Description: Retrieve a dataframe of OpEx transactions for a specific month.
    
- Get OpEx DataFrame by Year
  - URL: /api/opex-df-year/<year>/
  - Method: GET
  - Permission: IsAuthenticated
  - Description: Retrieve a dataframe of OpEx transactions for a specific year.

- Get CapEx and OpEx Percentage of Revenue
  - URL: /api/opex-capex-revenue/<year>/
  - Method: GET
  - Permission: IsAuthenticated
  - Description: Retrieve the percentage of revenue for CapEx and OpEx for a specific year.

### User Management Endpoints
- Register User

  - URL: /api/register/
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
  - URL: /api/users/
  - Method: GET
  - Permission: IsAdminUser
  - Description: List all users (admin only).

- Change Password
  - URL: /api/users/<pk>/change-password/
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
  - URL: /api/users/<pk>/
  - Method: DELETE
  - Permission: IsAdminUser
  - Description: Deactivate a user (admin only).

- Login
  - URL: /api-login/
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
  - URL: /api-logout/
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
  - URL: /
  - Method: GET
  - Description: Home page.

- Login Page
  - URL: /login/
  - Method: GET, POST
  - Description: Login page for users.

- Logout
  - URL: /logout/
  - Method: POST
  - Description: Logout the user.

- Chart Visualization
  - URL: /chart/
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
