from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.ReverseDnsView.as_view(), name='reverse-dns-form'),
]
