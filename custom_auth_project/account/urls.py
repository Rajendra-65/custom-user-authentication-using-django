from django.urls import path,include
from account.views import register

urlpatterns = [
    path('register/',register,name='register')
]
