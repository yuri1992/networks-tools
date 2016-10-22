from django.db import models


class ReverseDnsLog(models.Model):
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    ip_requested = models.GenericIPAddressField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
