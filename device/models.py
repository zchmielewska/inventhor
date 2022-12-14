from django.conf import settings
from django.db import models

ACTION = (
    (1, "ADD"),
    (2, "REMOVE"),
)


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["last_name"]


class Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Device(models.Model):
    local_id = models.PositiveIntegerField()
    model = models.CharField(max_length=64)
    usable = models.BooleanField(default=True)
    comment = models.TextField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} {self.local_id} ({self.model})"

    class Meta:
        ordering = ["local_id"]


class Log(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    action = models.IntegerField(choices=ACTION)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
