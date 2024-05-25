from django.shortcuts import render, HttpResponse
from django.views import View
from User.models import User

class Index(View):
    def get(self, request):
        user = User.objects.all()[0]
        context = {
            'fullname': user.firstname + user.lastname,
            'title': user.title,
            'email': user.email,
            'avatar': user.avatar.url,
            'aboutme': user.aboutme
        }
        return render(request, 'Main/index.html', context=context)