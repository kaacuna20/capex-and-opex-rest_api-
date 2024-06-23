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
            is_active = False
        )
        
        return user