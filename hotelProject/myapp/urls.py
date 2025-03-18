from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('api/employees/', views.employee_list_api, name='employee_list_api'),
    path('api/employees/create/', views.employee_create_api, name='employee_create_api'),
    path('api/employees/<str:employee_id>/update/', views.employee_update_api, name='employee_update_api'),
    path('api/employees/<str:employee_id>/delete/', views.employee_delete_api, name='employee_delete_api'),
]