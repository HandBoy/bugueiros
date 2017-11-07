from django.conf.urls import url
from .views import index, dashboard

urlpatterns = [
    url(r'^$', view=index, name='index'),
    url(r'^dashboard/$', view=dashboard, name='dashboard'),
]
