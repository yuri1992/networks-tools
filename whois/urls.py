from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.WhoisView.as_view(), name='whois-form'),
]
