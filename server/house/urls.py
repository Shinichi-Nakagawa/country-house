from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from house import views


urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^records/$', views.RecordList.as_view(), name='record-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)