from django import forms

from device import models


class DeviceForm(forms.ModelForm):
    class Meta:
        model = models.Device
