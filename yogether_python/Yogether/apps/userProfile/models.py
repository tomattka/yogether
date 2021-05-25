from django.contrib.auth.models import AbstractUser
from django.db import models


class YgUser(AbstractUser):
    """ Custom user model """
    profile_pic = models.ImageField(upload_to='user/profile_pic', blank=True, null=True)
    gender = models.IntegerField(null=True)
    phone = models.CharField(max_length=25, null=True)
    is_online = models.BooleanField(default=False, null=True)
    social_data_loaded = models.BooleanField(default=False, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class YgUserInfo(models.Model):
    user = models.OneToOneField(YgUser, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField(null=True)
    about = models.TextField(null=True)
    request = models.CharField(max_length=1000, null=True)
    links = models.CharField(max_length=2000, null=True)
    location = models.CharField(max_length=100, null=True)  # !!! Change later to FK
    marital_status = models.CharField(max_length=20, null=True)
    experience = models.CharField(max_length=500, null=True)  # !!! Change later to FK or sth

    class Meta:
        verbose_name = "Данные пользователя"

