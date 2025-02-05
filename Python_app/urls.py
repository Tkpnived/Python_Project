from django.urls import path
from . import views

urlpatterns = [
    path('blog_list/', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('new/', views.blog_create, name='blog_create'),
    path('<int:pk>/edit/', views.blog_update, name='blog_update'),
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),

    path('', views.register, name='register'),
    path('custom_login', views.custom_login, name='custom_login'),
    path('custom_logout', views.custom_logout, name='custom_logout'),

]
