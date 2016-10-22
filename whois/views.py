import subprocess

from django.shortcuts import render_to_response
from django.views.generic import FormView
from ipware.ip import get_real_ip

from whois.forms import WhoisForm
from whois.models import WhoisLog


def run_whois_lookup(url):
    try:
        out = subprocess.check_output(["whois", url])
        return out
    except Exception as e:
        return None


class WhoisView(FormView):
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
        reversed_host = run_whois_lookup(url_requested)

        return render_to_response('whois_completed.html', {
            'reversed_host': reversed_host,
        })
