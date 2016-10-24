from django.contrib import admin

from network_utils.models import PingLog


class PingLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(PingLog, PingLogAdmin)
