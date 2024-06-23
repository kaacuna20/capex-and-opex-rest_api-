from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
#from faker import Faker

class TestSetup(APITestCase):
    
    def setUp(self):
        #faker = Faker()
        self.user = User.objects.create_superuser(
            username="test_username",#faker.name(),
            password='testpassword',
            email="test@email.com"#faker.email()
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
       
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        return super().setUp()
        
    #def test_print_token(self):
    #    print(self.token)