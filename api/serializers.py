from rest_framework import serializers
from .models import *


###### CAPEX/OPEX SERIALIZERS ######
class CapexTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapexTransaction
        fields = "__all__"
    
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "date": instance.date,
            "description": instance.description,
            "amount": instance.amount,
            "status": instance.status,
            "category": instance.category,
            "contractor": instance.contractor.name,
            "user_project": instance.user_project.username
        }
        
class OpexTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpexTransaction
        fields = "__all__"
    
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "date": instance.date,
            "description": instance.description,
            "amount": instance.amount,
            "status": instance.status,
            "category": instance.category,
            "contractor": instance.contractor.name,
            "user_planner": instance.user_planner.username
        }
        


