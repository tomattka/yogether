import urllib.request
from urllib.parse import urlparse
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from allauth.account.signals import user_logged_in  #user_signed_up later - ?
from django.dispatch import receiver
from datetime import datetime

from PIL import Image


def auto_cut_image(img, size=270):
    pil_img = Image.open(img)
    img_width, img_height = pil_img.size
    img_lengh = img_width
    if img_height < img_width:
        # широкая
        img_lengh = img_height
        top = 0
        left = (img_width - img_lengh) // 2
    else:
        # высокая
        top = (img_height - img_lengh) // 2
        left = 0
    pil_img = pil_img.crop((left, top, left + img_lengh, top + img_lengh))
    pil_img = pil_img.resize((size, size))
    pil_img.save(img.path)


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
        # location = extra_data['country']['title']  # Добавить проверку на город
        gender = extra_data['sex']  # Добавить приведение пола к словарю
        profile_pic_url = extra_data['photo_max_orig']

        # -------------------- Getting image -------------------
        if profile_pic_url:
            img_temp = NamedTemporaryFile()
            img_temp.write(urllib.request.urlopen(profile_pic_url).read())
            img_temp.flush()

            img_name = urlparse(profile_pic_url).path.split('/')[-1]
            user_yg.profile_pic.save(img_name, File(img_temp))
            auto_cut_image(user_yg.profile_pic)

        # --------------------- Saving data -------------------

        user_info.birth_date = datetime.strptime(birth_date, '%d.%m.%Y')
        user_yg.social_data_loaded = True

        user_info.save()
        user_yg.save()

        print("Data saved")

    else:
        print("Data already existed")
