from django import forms

from device import models


class DeviceForm(forms.ModelForm):
    class Meta:
        model = models.Device
        fields = ["type", "local_id", "model", "employee", "usable", "comment"]
