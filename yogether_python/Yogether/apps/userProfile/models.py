from django.contrib.auth.models import AbstractUser
from django.db import models


class YgGender(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "Гендер"


class YgLocation(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "Местоположение"


class YgMaritalStatus(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "Семейное положение"


class YgExperience(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "Опыт практики"


class YgDoctrine(models.Model):
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=1000, blank=True, null=True)
    full_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Учение"
        verbose_name_plural = "Учения"


class YgTradition(models.Model):
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=1000, blank=True, null=True)
    full_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Традиция"
        verbose_name_plural = "Традиции"


class YgPractice(models.Model):
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=1000, blank=True, null=True)
    full_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Практика"
        verbose_name_plural = "Практики"


class YgInterest(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Интерес"
        verbose_name_plural = "Интересы"


class YgUser(AbstractUser):
    """ Custom user model """
    profile_pic = models.ImageField(upload_to='user/profile_pic', blank=True, null=True)
    gender = models.ForeignKey(YgGender, on_delete=models.SET_NULL, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    is_online = models.BooleanField(default=False, null=True)
    social_data_loaded = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.username + ' (' + self.first_name + ' ' + self.last_name + ')'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class YgUserInfo(models.Model):
    user = models.OneToOneField(YgUser, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    request = models.CharField(max_length=1000, blank=True, null=True)
    location = models.ForeignKey(YgLocation, on_delete=models.SET_NULL, blank=True, null=True)
    marital_status = models.ForeignKey(YgMaritalStatus, on_delete=models.SET_NULL, blank=True, null=True)
    experience = models.ForeignKey(YgExperience, on_delete=models.SET_NULL, blank=True, null=True)
    doctrines = models.ManyToManyField(YgDoctrine, blank=True)
    traditions = models.ManyToManyField(YgTradition, blank=True)
    practices = models.ManyToManyField(YgPractice, blank=True)
    interests = models.ManyToManyField(YgInterest, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"



