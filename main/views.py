from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import FeedBackModel


# Create your views here.
class MainPageView(View):
    def get(self, request):
        return render(request, template_name='mainPage.html', context={})


class MainPageFeedbackView(View):
    def get(self, request):
        if request.method == 'POST':
            print(request.META)

    def post(self, request):
        print(request.META)
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        title = request.POST.get('title')
        message = request.POST.get('message')

        FeedBackModel.objects.create(name=name, tel=tel, title=title, message=message).save()

        return HttpResponse('good')
