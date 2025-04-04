from django.urls import path
from userapis import views

urlpatterns = [
    path('', views.login_data, name="login"),
    path('register/', views.register, name="register"),
    path('main/', views.main, name="main" ),
    path('cart/',views.cart,name="cart"),
    path('profile/',views.profile,name="profile"),
    path('logout/',views.logout_page,name="logout"),
    path('confirm/',views.confirm_logout, name="confirm"),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart')
    
]
