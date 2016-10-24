import requests
from django.shortcuts import render_to_response
from django.views.generic import FormView
from ipware.ip import get_real_ip

from dns_tools.shell_commands import run_reverse_dns, run_whois_lookup, run_dns_lookup
from forms import ReverseDnsForm, WhoisForm, DnsLookupForm, IPtoDomainForm
from models import ReverseDnsLog, WhoisLog, DnsLog, IPToDomainLog, IPToDomain


class FormViewWithRequest(FormView):
    def get_form_kwargs(self):
        kwargs = super(FormViewWithRequest, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class IPtoDomainView(FormViewWithRequest):
    template_name = 'ip_domain_form.html'
    form_class = IPtoDomainForm

    def fetch_reverse(self, ip_requested):
        out = set()

        # Fetching our local data for the current IP
        qs = IPToDomain.objects.filter(ip_host=ip_requested)
        if qs.exists():
            out = out.union(qs.values_list('url', flat=True))

        # Decide if we need to go for external source
        if not IPToDomainLog.objects.filter(ip_requested=ip_requested).exists():
            req = requests.get('http://api.hackertarget.com/reverseiplookup/',
                               params={'q': ip_requested})

            raw_data = req.content.split()
            if raw_data:
                IPToDomain.objects.bulk_create([IPToDomain(url=url, ip_host=ip_requested) for url in raw_data])
                out = out.union(raw_data)

        return list(out)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        ip_requested = form.cleaned_data['ip_requested']
        command_output = self.fetch_reverse(ip_requested)
        IPToDomainLog.objects.create(user_ip=get_real_ip(self.request),
                                     ip_requested=ip_requested)

        return render_to_response('ip_domain_completed.html', {
            'url_list': command_output,
            'ip_requested': ip_requested,
        })


class DnsLookupView(FormViewWithRequest):
    template_name = 'dns_form.html'
    form_class = DnsLookupForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        url_requested = form.cleaned_data['url_requested']
        DnsLog.objects.create(user_ip=get_real_ip(self.request),
                              url_requested=url_requested)
        command_output = run_dns_lookup(url_requested)

        return render_to_response('dns_completed.html', {
            'command_output': command_output,
            'url_requested': url_requested,
        })


class ReverseDnsView(FormViewWithRequest):
    template_name = 'reverse_form.html'
    form_class = ReverseDnsForm

    def get_form_kwargs(self):
        kwargs = super(ReverseDnsView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        ip_requested = form.cleaned_data['ip_requested']
        ReverseDnsLog.objects.create(user_ip=get_real_ip(self.request),
                                     ip_requested=ip_requested)
        reversed_host = run_reverse_dns(ip_requested)

        return render_to_response('reverse_completed.html', {
            'reversed_host': reversed_host,
            'ip_requested': ip_requested,
        })


class WhoisView(FormViewWithRequest):
    template_name = 'whois_form.html'
    form_class = WhoisForm

    def get_form_kwargs(self):
        kwargs = super(WhoisView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        url_requested = form.cleaned_data['url_requested']
        WhoisLog.objects.create(user_ip=get_real_ip(self.request),
                                url_requested=url_requested)
        whois_result = run_whois_lookup(url_requested)

        return render_to_response('whois_completed.html', {
            'url_requested': url_requested,
            'whois_result': whois_result
        })
