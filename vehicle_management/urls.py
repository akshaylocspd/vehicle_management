from django.contrib import admin
from django.urls import path
from vehicles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage,name='homePage'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('vehicles/register/', views.register_vehicle, name='register_vehicle'),
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicles/edit/<int:pk>/', views.edit_vehicle, name='edit_vehicle'),
    path('chalans/add/', views.add_chalan, name='add_chalan'),
    path('chalans/', views.chalan_list, name='chalan_list'),
    path('chalans/edit/<int:pk>/', views.edit_chalan, name='edit_chalan'),
]


