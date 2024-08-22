from django.urls import path
from .views import (
    home_view, 
    SignupView, 
    logout_view, 
    register_entry_view, 
    employee_list, 
    employee_create, 
    employee_update, 
    employee_delete, 
    visitor_list, 
    visitor_create, 
    visitor_update, 
    visitor_delete,
    attendance_report,
    evacuation_report
)

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', SignupView.as_view(), name='signup'), 
    path('logout/', logout_view, name='logout'),
    path('register_entry/', register_entry_view, name='register_entry'),
    path('employees/', employee_list, name='employees'),
    path('employees/new/', employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', employee_delete, name='employee_delete'),
    path('visitors/', visitor_list, name='visitors'),
    path('visitors/new/', visitor_create, name='visitor_create'),
    path('visitors/<int:pk>/edit/', visitor_update, name='visitor_update'),
    path('visitors/<int:pk>/delete/', visitor_delete, name='visitor_delete'),
    path('attendance-report/', attendance_report, name='attendance_report'),
    path('evacuation-report/', evacuation_report, name='evacuation_report'),

]
