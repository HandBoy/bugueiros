from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import JSONRenderer

from .serializers import UserSerializer, TravelSerializer, ScheduleSerializer
from ..bugueiro.models import Travel, Schedule, QueueSchedule

from datetime import date

# Create your views here.


class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=['post'])
    def login(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                #request.session['auth'] = token.key
                return Response({"token": token})
            else:
                return Response({"error": "Login failed"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Login failed"}, status=status.HTTP_401_UNAUTHORIZED)


class UsersViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


def get_auth_token(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            request.session['auth'] = token.key
            return redirect('/polls/', request)
    return redirect(settings.LOGIN_URL, request)


class UserLogin(APIView):
    permission_classes = []
    authentication_classes = []
    """
    List all snippets, or create a new snippet.
    """
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)
        user = get_object_or_404(User, pk=user.pk)
        serializer = UserSerializer(user)
        serializer.token = token.key
        return Response(serializer.data, status=status.HTTP_200_OK)


class TravelViewSet(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = []

    def post(self, request, format=None):
        serializer = TravelSerializer(data=request.data)

        if serializer.is_valid():
            travel = serializer.save()
            return Response({"travel": travel.pk})


    def post(self, request, pk, format=None):
        queryset = QueueSchedule.objects.filter(schedule=pk)



class ScheduleViewSet(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = []

    def get(self, request, format=None):
        schedule = Schedule.objects.filter(created_date__day=date.today().day)
        serializer = ScheduleSerializer(schedule, many=True)
        #json = JSONRenderer().render(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
