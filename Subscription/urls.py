from django.conf.urls import url
from . import views

'''
Beschrijft welke url welke view oproept
'''

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reports/download_report/', views.download_report, name='download_report'),
    url(r'^reports/', views.reports, name='reports'),
    url(r'^subscribe/', views.subscribe, name='subscribe'),
    url(r'^succes/(?P<saved>\b(True|False)\b)/$', views.succes, name='succes'),
]
