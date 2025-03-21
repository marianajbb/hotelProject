from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)



urlpatterns = [
    path('api/employees/', views.employee_list_api, name='employee-list-api'),
    path('api/employees/create/', views.employee_create_api, name='employee-create-api'),
    path('api/employees/<str:employee_id>/', views.employee_detail_api, name='employee-detail-api'),
    path('api/employees/update/<str:employee_id>/', views.employee_update_api, name='employee-update-api'), #Add this line
    path('api/employees/delete/<str:employee_id>/', views.employee_delete_api, name='employee-delete-api'), #Add this line
    path("service/", include(router.urls)),
    path('employees/', views.employee_list_view, name='employee-list'),
    path('users/login', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]