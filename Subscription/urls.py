from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reports/', views.reports, name='reports'),
    url(r'^reports/download_report/', views.download_report, name='download_report'),
    url(r'^subscribe/', views.subscribe, name='subscribe'),
    url(r'^succes/(?P<saved>\b(True|False)\b)/$', views.succes, name='succes'),
]
