from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
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