from django.urls import path
from user.views import TestView, RegisterView, LoginView


urlpatterns = [
    path('test', TestView.as_view(), name='test'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
]
