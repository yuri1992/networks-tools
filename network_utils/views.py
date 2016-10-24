from django.shortcuts import render_to_response
from ipware.ip import get_real_ip

from dns_tools.shell_commands import run_ping_query, run_traceroute_query
from network_utils.forms import PingForm, TracerouteForm
from network_utils.models import PingLog, TracerouteLog
from networks_tools.views import FormViewWithRequest


class PingView(FormViewWithRequest):
    template_name = 'ping_form.html'
    form_class = PingForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        host = form.cleaned_data['host']
        PingLog.objects.create(user_ip=get_real_ip(self.request),
                               host=host)
        command_output = run_ping_query(host)

        return render_to_response('ping_completed.html', {
            'command_output': command_output,
            'host': host,
        })


class TracerouteView(FormViewWithRequest):
    template_name = 'traceroute_form.html'
    form_class = TracerouteForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        host = form.cleaned_data['host']
        TracerouteLog.objects.create(user_ip=get_real_ip(self.request),
                               host=host)
        command_output = run_traceroute_query(host)

        return render_to_response('traceroute_completed.html', {
            'command_output': command_output,
            'host': host,
        })