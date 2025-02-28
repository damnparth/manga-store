from django.urls import path
from userapis import views

urlpatterns = [
    path('', views.login_data, name="login"),
    path('register/', views.register, name="register"),
    path('main/', views.main, name="main" )
    
]
