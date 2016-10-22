from django.contrib import admin

from reverse_dns.models import ReverseDnsLog


class ReverseDnsLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(ReverseDnsLog, ReverseDnsLogAdmin)
