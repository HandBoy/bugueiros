from django.conf.urls import url
from .views import index, dashboard, update_profile, profile, signup

urlpatterns = [
    url(r'^$', view=index, name='index'),
    url(r'^dashboard/$', view=dashboard, name='dashboard'),
    url(r'^dashboard/user/register/$', view=signup, name='register'),
    url(r'^dashboard/user/profile/(?P<pk>[0-9]+)/$', view=profile, name='profile'),
]
