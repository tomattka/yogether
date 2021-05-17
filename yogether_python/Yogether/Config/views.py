from django.views.generic.base import View
from django.shortcuts import render


class MainPage(View):

    def get(self, request):
        return render(request, 'profile/tplProfile.html', {})
