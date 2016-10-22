import subprocess

from django.shortcuts import render_to_response
from django.views.generic import FormView
from ipware.ip import get_real_ip

from forms import ReverseDnsForm
from models import ReverseDnsLog


def run_reverse_dns(ip):
    try:
        out = subprocess.check_output(["host", ip])
        reversed_host = out.split()[-1]
        return reversed_host
    except Exception:
        return None


class ReverseDnsView(FormView):
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
        })
