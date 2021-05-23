from django.shortcuts import render
from django.views.generic.base import View
from .forms import YGLoginForm


class UserProfile(View):
    def get(self, request):
        return render(request, "ygProfile/tplProfile.html", {"form" : YGLoginForm})
