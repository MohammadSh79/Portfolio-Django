from django.shortcuts import render, HttpResponse
from django.views import View

class Index(View):
    def get(self, request):
        context = {
            
        }
        return render(request, 'Main/index.html', context=context)