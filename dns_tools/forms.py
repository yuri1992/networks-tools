from datetime import timedelta
from django.utils.timezone import now
from ipware.ip import get_real_ip

from django import forms
from django.conf import settings

from models import ReverseDnsLog, WhoisLog, IPToDomainLog
from networks_tools import consts


class DnsLookupForm(forms.Form):
    url_requested = forms.URLField()

    def __init__(self, *args, **kwargs):
        # important to "pop" added kwarg before call to parent's constructor
        self.request = kwargs.pop('request')
        super(DnsLookupForm, self).__init__(*args, **kwargs)

    def clean(self):
        # Checking if user is reached to his daily limit
        ip = get_real_ip(self.request)
        latest_calls = ReverseDnsLog.objects.filter(user_ip=ip,
                                                    created_at__gte=(now() - timedelta(days=1)))

        if latest_calls.count() > settings.REVERSE_DNS_DAILY_LIMIT:
            raise forms.ValidationError(consts.REVERSE_DNS_ERROR_REACHED)


class IPtoDomainForm(forms.Form):
    ip_requested = forms.GenericIPAddressField()

    def __init__(self, *args, **kwargs):
        # important to "pop" added kwarg before call to parent's constructor
        self.request = kwargs.pop('request')
        super(IPtoDomainForm, self).__init__(*args, **kwargs)

    def clean(self):
        # Checking if user is reached to his daily limit
        ip = get_real_ip(self.request)
        latest_calls = IPToDomainLog.objects.filter(user_ip=ip,
                                                    created_at__gte=(now() - timedelta(days=1)))

        if latest_calls.count() > settings.IP_TO_DOMAIN:
            raise forms.ValidationError(consts.REVERSE_DNS_ERROR_REACHED)



class ReverseDnsForm(forms.Form):
    ip_requested = forms.GenericIPAddressField()

    def __init__(self, *args, **kwargs):
        # important to "pop" added kwarg before call to parent's constructor
        self.request = kwargs.pop('request')
        super(ReverseDnsForm, self).__init__(*args, **kwargs)

    def clean(self):
        # Checking if user is reached to his daily limit
        ip = get_real_ip(self.request)
        latest_calls = ReverseDnsLog.objects.filter(user_ip=ip,
                                                    created_at__gte=(now() - timedelta(days=1)))

        if latest_calls.count() > settings.REVERSE_DNS_DAILY_LIMIT:
            raise forms.ValidationError(consts.REVERSE_DNS_ERROR_REACHED)


class WhoisForm(forms.Form):
    url_requested = forms.URLField()

    def __init__(self, *args, **kwargs):
        # important to "pop" added kwarg before call to parent's constructor
        self.request = kwargs.pop('request')
        super(WhoisForm, self).__init__(*args, **kwargs)

    def clean(self):
        # Checking if user is reached to his daily limit
        ip = get_real_ip(self.request)
        latest_calls = WhoisLog.objects.filter(user_ip=ip,
                                               created_at__gte=(now() - timedelta(days=1)))

        if latest_calls.count() > settings.WHOIS_DAILY_LIMIT:
            raise forms.ValidationError(consts.REVERSE_DNS_ERROR_REACHED)
