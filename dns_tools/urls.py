from django.conf.urls import url
import views

urlpatterns = [
    url(r'reverse-dns-lookup/$', views.ReverseDnsView.as_view(), name='reverse-dns-form'),
    url(r'dns-lookup/$', views.DnsLookupView.as_view(), name='dns-form'),
    url(r'ip-to-domains/$', views.IPtoDomainView.as_view(), name='ip-to-domains'),
    url(r'whois/$', views.WhoisView.as_view(), name='whois-form'),
]
