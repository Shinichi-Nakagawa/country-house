from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from house import views


urlpatterns = [
    url(r'^records/$', views.record_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)