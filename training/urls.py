from django.conf.urls import url

from . import views

urlpatterns = [
    #/training/
    url(r'^$', views.index, name='index'),
    #/training/<airline_id>
    url(r'^(?P<airline_id>[0-9]+)/results/$', views.detail, name='detail')
]


