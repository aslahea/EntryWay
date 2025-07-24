from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [

    # 👤 User Routes
    path('', views.welcome_view, name='welcome'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('soft-delete-user/<int:user_id>/',
         views.soft_delete_user, name='soft_delete_user'),

    
]
