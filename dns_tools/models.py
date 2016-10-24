from django.db import models


class ReverseDnsLog(models.Model):
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    ip_requested = models.GenericIPAddressField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class IPToDomainLog(models.Model):
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    ip_requested = models.GenericIPAddressField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class IPToDomain(models.Model):
    ip_host = models.GenericIPAddressField(null=False)
    url = models.URLField(null=False)
    since = models.DateTimeField(auto_now_add=True)


class DnsLog(models.Model):
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    url_requested = models.URLField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class WhoisLog(models.Model):
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    url_requested = models.URLField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
