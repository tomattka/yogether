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
        return render(request, "ygProfile/tplProfile.html", {"form" : YGLoginForm, "user_info": user_info})
