from django.contrib.auth.models import User
from rest_framework import serializers
from apps.bugueiro.models import Profile


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


