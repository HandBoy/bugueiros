from django.conf.urls import url
from .views import index, dashboard, update_profile, profile, signup, user_list, add_profile, initSchedule

urlpatterns = [
    url(r'^$', view=index, name='index'),
    url(r'^dashboard/$', view=dashboard, name='dashboard'),
    url(r'^dashboard/user/register/$', view=signup, name='register'),
    url(r'^dashboard/user/profile/(?P<pk>[0-9]+)/$', view=profile, name='profile'),
    url(r'^dashboard/user/add/$', view=add_profile, name='add_user'),
    url(r'^dashboard/user/update/(?P<pk>[0-9]+)/$', view=update_profile, name='update_profile'),
    url(r'^dashboard/user/list/$', view=user_list, name='users'),
    url(r'^dashboard/initSchedule/$', view=initSchedule, name='fila'),

]
