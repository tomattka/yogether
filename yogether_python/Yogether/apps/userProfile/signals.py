import urllib.request
from urllib.parse import urlparse
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from allauth.account.signals import user_logged_in  #user_signed_up later - ?
from django.dispatch import receiver
from datetime import datetime


@receiver(user_logged_in)
def my_callback(sender, user, **kwargs):
    user_id = user.id

    from .models import YgUser, YgUserInfo
    user_yg = YgUser.objects.filter(id=user_id)[0]

    if not user_yg.social_data_loaded and user.socialaccount_set.filter(provider='vk'):

        user_info = YgUserInfo(user_id=user_id)  # Добавлять при создании — ?
        if YgUserInfo.objects.filter(user_id=user_id):
            user_info = YgUserInfo.objects.filter(user_id=user_id)[0]

        # -------------------- Getting data -------------------

        user_dataset = user.socialaccount_set.filter(provider='vk')[0]
        extra_data = user_dataset.extra_data

        birth_date = extra_data['bdate']
        location = extra_data['country']['title']  # Добавить проверку на город
        # marital_status = "" - позже сделать
        gender = extra_data['sex']  # Добавить приведение пола к словарю
        profile_pic_url = extra_data['photo_max_orig']

        # -------------------- Getting image -------------------
        if profile_pic_url:
            img_temp = NamedTemporaryFile()
            img_temp.write(urllib.request.urlopen(profile_pic_url).read())
            img_temp.flush()

            img_name = urlparse(profile_pic_url).path.split('/')[-1]
            user_yg.profile_pic.save(img_name, File(img_temp))

        # --------------------- Saving data -------------------

        user_info.birth_date = datetime.strptime(birth_date, '%d.%m.%Y')
        # user_info.location = location
        # user_yg.gender = gender !!! Change
        user_yg.social_data_loaded = True

        user_info.save()
        user_yg.save()

        print("Data saved")

    else:
        print("Data already existed")
