from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from device import models


class MainView(View):
    def get(self, request):
        devices = models.Device.objects.all()
        return render(request, "device/main.html", {"devices": devices})


class DeviceCreateView(CreateView):
    model = models.Device
    fields = ['type', 'local_id', 'model', 'usable', 'comment', 'employee']
    success_url = '/'


class DeviceUpdateView(UpdateView):
    model = models.Device
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/'


class DeviceDeleteView(DeleteView):
    model = models.Device
    success_url = reverse_lazy('main')


class DeviceDetailView(View):
    def get(self, request, pk):
        device = get_object_or_404(models.Device, id=pk)
        return render(request, "device/device_detail.html", {"device": device})


class EmployeeListView(View):
    def get(self, request):
        employees = models.Employee.objects.all()
        return render(request, "device/employee_list.html", {"employees": employees})


class EmployeeCreateView(CreateView):
    model = models.Employee
    fields = '__all__'
    success_url = '/employee/'


class EmployeeUpdateView(UpdateView):
    model = models.Employee
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/employee/'


class EmployeeDeleteView(DeleteView):
    model = models.Employee
    success_url = reverse_lazy('employee_list')


class EmployeeDetailView(View):
    def get(self, request, pk):
        employee = get_object_or_404(models.Employee, id=pk)
        return render(request, "device/employee_detail.html", {"employee": employee})
