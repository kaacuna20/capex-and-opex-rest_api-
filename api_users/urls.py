from django.urls import path
from . import views

urlpatterns = [
    
    path("register/", views.CreateUserView.as_view(), name="register"),
    path("list-users", views.ListUserView.as_view(), name="list-users"),
    path("change-password/<int:pk>", views.ChangePassword.as_view(), name="change-password"),
    path("delete/<int:pk>", views.UserDestroyAPIView.as_view(), name="delete-user"),
    
    
]