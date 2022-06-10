from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LogIn.as_view(), name='login')
]
