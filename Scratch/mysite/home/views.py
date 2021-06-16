from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from django.middleware.csrf import get_token
from . models import questions

def index(request):
    return HttpResponse("Hello worlds youre at the polls index.")

def index2(request):
    return HttpResponse("i got a new car")

class myrequest(View):

    def get(self, request):
        get_token(request)
        response = { 'Get Request' : 'OK'}
        return JsonResponse(response,safe=False)  

    def post(self, request):
        print('Got Post')
        a=str(request.POST.get('question'))
        print(a)

        b=questions(question_text = a)
        b.save()

        print(b)

        response = { 'Get Request' : 'OK'}
        return JsonResponse(response,safe=False) 

