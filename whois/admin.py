from django.contrib import admin

from whois.models import WhoisLog


class WhoisLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(WhoisLog, WhoisLogAdmin)
