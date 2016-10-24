from datetime import timedelta

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.core.validators import validate_ipv46_address
from django.utils.timezone import now
from ipware.ip import get_real_ip

from network_utils.models import PingLog, TracerouteLog
from networks_tools import consts
from networks_tools.forms import FormWithRequest


class IPOrUrlField(forms.CharField):
    def validate(self, value, **kwargs):
        url_validator = URLValidator()
        try:
            url_validator(value)
        except ValidationError:
            try:
                validate_ipv46_address(value)
            except ValidationError:
                return False

        return True


class TracerouteForm(FormWithRequest):
    host = IPOrUrlField()

    def clean(self):
        # Checking if user is reached to his daily limit
        ip = get_real_ip(self.request)
        latest_calls = TracerouteLog.objects.filter(user_ip=ip,
                                                    created_at__gte=(now() - timedelta(days=1)))

        if latest_calls.count() > settings.TRACEROUTE_DAILY_LIMIT:
            raise forms.ValidationError(consts.TRACEROUTE_ERROR_LIMIT_REACHED)


class PingForm(FormWithRequest):
    host = IPOrUrlField()

    def clean(self):
        # Checking if user is reached to his daily limit
        ip = get_real_ip(self.request)
        latest_calls = PingLog.objects.filter(user_ip=ip,
                                              created_at__gte=(now() - timedelta(days=1)))

        if latest_calls.count() > settings.PING_DAILY_LIMIT:
            raise forms.ValidationError(consts.PING_ERROR_LIMIT_REACHED)
