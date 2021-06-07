from re import match

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



        # -------- City/country ---------

        location = extra_data.get('city')
        if not location:
            location = extra_data.get('country')
        if location:
            location = location.get('title')
            # Saving to database
            from .models import YgLocation
            yg_location = YgLocation.objects.get(title__iexact=location) #case insensitive
            if not yg_location:
                yg_location = YgLocation(title=location)
                yg_location.save()
            user_info.location = yg_location
        else:
            user_info.location = None

        # -------- Birth date ---------
        if extra_data['bdate']:
            birth_date = extra_data['bdate']
            user_info.birth_date = datetime.strptime(birth_date, '%d.%m.%Y')

        # -------- Gender ---------
        if extra_data['sex']:
            gender = extra_data['sex']  # Добавить приведение пола к словарю
            if gender == 1:
                gender = 'Женский'
            else:
                gender = 'Мужской'
            from .models import YgGender
            yg_gender = YgGender.objects.get(title__iexact=gender)
            user_yg.gender = yg_gender

        # -------- Marital status ---------
        relation = extra_data['relation']
        if relation:
            status = {  # статусы контакта
                1: 'свободен',  # не замужем
                2: 'в отношениях',
                3: 'в отношениях',
                4: 'женат',  # замужем
                5: 'в отношениях',
                6: 'в поиске', # в активном поиске
                7: 'в отношениях',
                8: 'в отношениях'
            }.get(relation)

            from .models import YgMaritalStatus
            yg_status = YgMaritalStatus.objects.get(title__iexact=status)
            user_info.marital_status = yg_status

            # -------------------- Getting image -------------------

        profile_pic_url = extra_data['photo_max_orig']

        if profile_pic_url and 'camera_400.png' not in profile_pic_url:
            img_temp = NamedTemporaryFile()
            img_temp.write(urllib.request.urlopen(profile_pic_url).read())
            img_temp.flush()

            img_name = urlparse(profile_pic_url).path.split('/')[-1]
            user_yg.profile_pic.save(img_name, File(img_temp))
            auto_cut_image(user_yg.profile_pic)

        # --------------------- Saving data -------------------


        user_yg.social_data_loaded = True

        user_info.save()
        user_yg.save()

        print("Data saved")

    else:
        print("Data already existed")
