from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Create your models here.


def get_upload_path_foto_perfil(instance, filename):
    import os
    return os.path.join("uploads/foto-perfil", filename)


class Permission(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to=get_upload_path_foto_perfil, null=True, blank=True)
    permission = models.ForeignKey(Permission, default=5)
    GENDER = ((1, 'Masculino'),(2, 'Feminino'),)
    gender = models.IntegerField(choices=GENDER, default=1, )

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    @receiver(post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class Travel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="travel")
    trip = models.ForeignKey('self', blank=True, null=True)
    latitude = models.TextField(max_length=100, blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    sequence = models.IntegerField()
    start = models.BooleanField(default=False)
    end = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


class Schedule(models.Model):
    version = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)


class QueueSchedule(models.Model):
    user = models.ForeignKey(User)
    schedule = models.ForeignKey(Schedule)
    position = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)