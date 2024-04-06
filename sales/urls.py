from django.urls import path
from .views import EmployeeStatisticsView, AllEmployeesStatisticsView, ClientStatisticsView

urlpatterns = [
    path('statistics/employee/<int:pk>/', EmployeeStatisticsView.as_view()),
    path('employee/statistics/', AllEmployeesStatisticsView.as_view()),
    path('statistics/client/<int:pk>/', ClientStatisticsView.as_view()),
]
