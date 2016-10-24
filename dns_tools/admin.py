from django.contrib import admin

from dns_tools.models import ReverseDnsLog, WhoisLog, IPToDomain, DnsLog, IPToDomainLog


class ReverseDnsLogAdmin(admin.ModelAdmin):
    pass


class WhoisLogAdmin(admin.ModelAdmin):
    pass

class DnsLogAdmin(admin.ModelAdmin):
    pass

class IPToDomainLogAdmin(admin.ModelAdmin):
    pass

class IPToDomainAdmin(admin.ModelAdmin):
    pass

admin.site.register(WhoisLog, WhoisLogAdmin)
admin.site.register(ReverseDnsLog, ReverseDnsLogAdmin)
admin.site.register(IPToDomain, IPToDomainAdmin)
admin.site.register(IPToDomainLog, IPToDomainLogAdmin)
admin.site.register(DnsLog, DnsLogAdmin)
