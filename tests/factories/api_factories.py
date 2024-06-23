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
            
            name = faker.company(),
            nit = str(faker.random_number(digits=11))
        )
        capex = CapexTransaction.objects.create(
            date = "2024-01-01",
            description = faker.text(),
            amount = 15000, 
            status = random.choice(STATUS_CHOICES),
            category = random.choice(CAPEX_CHOICES),
            contractor = contractor,
            user_project = user
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
            
            name = faker.company(),
            nit = str(faker.random_number(digits=11))
        )
        opex = OpexTransaction.objects.create(
            date = "2024-01-01",
            description = faker.text(),
            amount = 15000, 
            status = random.choice(STATUS_CHOICES),
            category = random.choice(OPEX_CHOICES),
            contractor = contractor,
            user_planner = user
        )
        
        return opex
    

class CapexRevenueFactory:
    def create_capex_revenue(self):
        capex_revenue = CapexRevenue.objects.create(
            revenue = 300000,
            date = "2024-01-01"
        )
        return capex_revenue


class OpexRevenueFactory:
    def create_opex_revenue(self):
        opex_revenue = OpexRevenue.objects.create(
            revenue = 400000,
            date = "2024-01-01"
        )
        return opex_revenue
    
