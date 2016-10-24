from django.db import models


class PingLog(models.Model):
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    host = models.CharField(null=False, max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)


class TracerouteLog(models.Model):
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    host = models.CharField(null=False, max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)


class GeoIPLog(models.Model):
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    ip_requested = models.CharField(null=False, max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)


class PortFowarding(models.Model):
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    ip_requested = models.CharField(null=False, max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
