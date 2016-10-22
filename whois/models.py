from django.db import models


class WhoisLog(models.Model):
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    url_requested = models.URLField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
