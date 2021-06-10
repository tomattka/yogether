from django.shortcuts import render
from django.views.generic.base import View
from .forms import YGLoginForm
from .models import YgUser, YgUserInfo
from django.db.models import Q
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt


class UserProfile(View):
    def get(self, request):
        user_id = request.user.id
        user_info = {}
        if YgUserInfo.objects.filter(user_id=user_id):
            user_info = YgUserInfo.objects.get(user_id=user_id)

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

            # Выводим феминитивы при необходимости
            user_info.str_mar_status = str(user_info.marital_status)
            if (str(request.user.gender) == 'Женский') and user_info.marital_status.title_fem:
                user_info.str_mar_status = user_info.marital_status.title_fem

        return render(request, "ygProfile/_user-info.html", {"form" : YGLoginForm, "user_info": user_info})


class LoginCheck(View):

    @csrf_exempt
    def get(self, request):
        username = request.GET.get('username', None)
        password = request.GET.get('password', None)
        result = 'no user'

        check_if_user_exists = YgUser.objects.filter(Q(username=username) | Q(email=username)).exists()
        if check_if_user_exists:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                result = 'ok'
            else:
                result = 'wrong password'

        return render(request, 'ygProfile/login-check.html', {'result': result})
