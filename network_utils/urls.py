from django.conf.urls import url
import views

urlpatterns = [
    url(r'ping/$', views.PingView.as_view(), name='ping-form'),
    url(r'traceroute/$', views.TracerouteView.as_view(), name='traceroute-form'),
]
