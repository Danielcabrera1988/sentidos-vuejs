from django.urls import path
""" from .api import UserAPIView, user_apiview, userdetailView """ 
from applications.user.views import RegisterAPI 
from knox import views as knox_views
from applications.user.views import LoginAPI

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

