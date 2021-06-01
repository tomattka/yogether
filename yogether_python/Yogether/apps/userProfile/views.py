from django.shortcuts import render
from django.views.generic.base import View
from .forms import YGLoginForm
from .models import YgUserInfo


class UserProfile(View):
    def get(self, request):
        user_id = request.user.id
        user_info = {}
        if YgUserInfo.objects.filter(user_id=user_id):
            user_info = YgUserInfo.objects.filter(user_id=user_id)[0]

            # !!! Позже, когда будут генериться конкретные ссылки, заменю простыню ниже
            # Учение
            res = '';
            for doctrine in user_info.doctrines.all():
                res += '<a href="#">' + doctrine.title + '</a>, '
            user_info.doctrine_list = res.removesuffix(', ')

            # Традиция
            res = '';
            for tradition in user_info.traditions.all():
                res += '<a href="#">' + tradition.title + '</a>, '
            user_info.tradition_list = res.removesuffix(', ')

            # Практики
            res = '';
            for practice in user_info.practices.all():
                res += '<a href="#">' + practice.title + '</a>, '
            user_info.practice_list = res.removesuffix(', ')

            # Интересы
            res = '';
            for interest in user_info.interests.all():
                res += '<a href="#">' + interest.title + '</a>, '
            user_info.interest_list = res.removesuffix(', ')

        return render(request, "ygProfile/tplProfile.html", {"form" : YGLoginForm, "user_info": user_info})
