from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


def get_upload_path_foto_perfil(instance, filename):
    import os
    return os.path.join("uploads/foto-perfil", filename)


class Permission(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    #photo = models.ImageField(upload_to=get_upload_path_foto_perfil, null=True, blank=True)
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