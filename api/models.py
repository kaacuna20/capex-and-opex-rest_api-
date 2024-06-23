from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = (
        ("in_process", 'In Process'),
        ("pending", 'Pending'),
        ("reject", 'Rejected'),
        ("aproved", 'Aproved'),
     )


class BaseTransaction(models.Model):
    date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

class BaseContractor(models.Model):
    name = models.CharField(max_length=255)
    nit = models.CharField(max_length=255, unique=True)
    

CAPEX_CHOICES = (
        ("equipment", 'Equipment'),
        ("building", 'Buildings'),
        ("technology", 'Technology'),
     )


class CapexContractor(BaseContractor):
    def __str__(self):
        return self.name

class CapexTransaction(BaseTransaction):
    category = models.CharField(max_length=100, choices=CAPEX_CHOICES)
    contractor = models.ForeignKey(CapexContractor, on_delete=models.SET_NULL, related_name="capex_contractor", null=True)
    user_project = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="user_project", null=True)

    def __str__(self):
        return f"{self.date} - {self.contractor.name} - ${self.amount}"
    
    
OPEX_CHOICES = (
        ("salaries", 'Salaries'),
        ("utilities", 'Utilities'),
        ("rent", 'Rent'),
     )

class OpexContractor(BaseContractor):
    def __str__(self):
        return self.name

class OpexTransaction(BaseTransaction):
    category = models.CharField(max_length=100, choices=OPEX_CHOICES)
    contractor = models.ForeignKey(OpexContractor, on_delete=models.SET_NULL, related_name="opex_contractor", null=True)
    user_planner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="user_planner", null=True)

    def __str__(self):
        return f"{self.date} - {self.contractor.name} - ${self.amount}"

class CapexRevenue(models.Model):
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.date} - ${self.revenue}"

class OpexRevenue(models.Model):
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.date} - ${self.revenue}"

