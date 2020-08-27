from django.urls import path
from . import views

app_name = 'userprofile'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    # 用户删除
    path('delete/<int:pk>/', views.user_delete, name='delete'),
    path('edit/<int:pk>/', views.profile_edit, name='edit'),
]
