from django.contrib.auth.models import User
from rest_framework import serializers
from apps.bugueiro.models import Profile, Travel, Schedule, QueueSchedule


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'profile', 'token')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_token(self, obj):
        return self.token


class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'


# MELHORAR PARA NÂO USAR O USERNAMESESIALIZER
class QueueScheduleSerializer(serializers.ModelSerializer):
    user = UsernameSerializer(many=False)

    class Meta:
        model = QueueSchedule
        fields = ('user', 'position','schedule')
        depth = 1
        ordering = ['position']


class ScheduleSerializer(serializers.ModelSerializer):
    queue = QueueScheduleSerializer(many=True)

    class Meta:
        model = Schedule
        fields = '__all__'



