from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from .views import get_auth_token, UserLogin, LoginViewSet, TravelViewSet



router = DefaultRouter()
#router.register(r'^login/$', LoginViewSet.login, base_name=LoginViewSet),
#router.register(r'^auth/$',  login_form, base_name=UserViewSet),

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^loginv2/$', csrf_exempt(LoginViewSet.login)),
    url(r'^get_auth_token/$', views.obtain_auth_token),
    url(r'^token/$', get_auth_token),
    url(r'^login/$', UserLogin.as_view()),
    url(r'^travel/$', TravelViewSet.as_view()),
]
