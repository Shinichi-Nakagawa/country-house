from django.conf.urls import patterns, include, url
from house import views


urlpatterns = [
    url(r'^records/$', views.record_list),
]