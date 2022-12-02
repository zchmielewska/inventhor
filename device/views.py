from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from device import forms, models


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        devices = models.Device.objects.all()
        return render(request, "device/main.html", {"devices": devices})


class DeviceCreateView(LoginRequiredMixin, CreateView):
    def get(self, request):
        form = forms.DeviceForm()
        return render(request, "device/device_form.html", {"form": form})

    def post(self, request):
        form = forms.DeviceForm(request.POST)
        if form.is_valid():
            device = form.save()

            # Employee has received the device
            if device.employee:
                log = models.Log(
                    employee=device.employee,
                    device=device,
                    action=1,
                    user=request.user,
                )
                log.save()
        return redirect(reverse_lazy("main"))


class DeviceUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        device = get_object_or_404(models.Device, pk=pk)
        form = forms.DeviceForm(instance=device)
        return render(request, "device/device_update_form.html", {"form": form})

    def post(self, request, pk):
        device = get_object_or_404(models.Device, pk=pk)
        form = forms.DeviceForm(request.POST, instance=device)

        if form.is_valid():
            device_new = form.save(commit=False)
            device_old = models.Device.objects.get(pk=pk)

            # Device has changed an employee
            if device_new.employee != device_old.employee:

                # Device has been removed from an employee
                if device_old.employee:
                    log = models.Log(
                        employee=device_old.employee,
                        device=device_new,
                        action=2,
                        user=request.user,
                    )
                    log.save()

                # Device has been added to an employee
                if device_new.employee:
                    log = models.Log(
                        employee=device_new.employee,
                        device=device_new,
                        action=1,
                        user=request.user,
                    )
                    log.save()

            device_new.save()
        return redirect(reverse_lazy("main"))


class DeviceDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Device
    success_url = reverse_lazy('main')


class DeviceDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        device = get_object_or_404(models.Device, id=pk)
        logs = models.Log.objects.filter(device=device)
        return render(request, "device/device_detail.html", {"device": device, "logs": logs})


class EmployeeListView(LoginRequiredMixin, View):
    def get(self, request):
        employees = models.Employee.objects.all()
        return render(request, "device/employee_list.html", {"employees": employees})


class EmployeeCreateView(LoginRequiredMixin, View):
    model = models.Employee
    fields = '__all__'
    success_url = '/employee/'


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Employee
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/employee/'


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Employee
    success_url = reverse_lazy('employee_list')


class EmployeeDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        employee = get_object_or_404(models.Employee, id=pk)
        logs = models.Log.objects.filter(employee=employee)
        return render(request, "device/employee_detail.html", {"employee": employee, "logs": logs})


class LogListView(LoginRequiredMixin, View):
    def get(self, request):
        logs = models.Log.objects.all()
        return render(request, "device/log_list.html", {"logs": logs})
