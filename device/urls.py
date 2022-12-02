from django.urls import path

from device import views

urlpatterns = [
    path('', views.MainView.as_view(), name="main"),
    path('device/add/', views.DeviceCreateView.as_view(), name="add_device"),
    path('device/update/<pk>', views.DeviceUpdateView.as_view(), name="update_device"),
    path('device/delete/<pk>', views.DeviceDeleteView.as_view(), name="delete_device"),
    path('device/detail/<pk>', views.DeviceDetailView.as_view(), name="device_detail"),

    path('employee/', views.EmployeeListView.as_view(), name="employee_list"),

    path('employee/add/', views.EmployeeCreateView.as_view(), name="add_employee"),
    path('employee/update/<pk>', views.EmployeeUpdateView.as_view(), name="update_employee"),
    path('employee/delete/<pk>', views.EmployeeDeleteView.as_view(), name="delete_employee"),
    path('employee/detail/<pk>', views.EmployeeDetailView.as_view(), name="employee_detail"),

    path('log/', views.LogListView.as_view(), name="log_list"),
]



