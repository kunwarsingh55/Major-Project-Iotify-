from django.urls import path

from . import views

from home.views import myrequest



urlpatterns = [
    path('', views.index, name='index'),
    path('car', views.index2, name='index2'),
    path('requesturl', myrequest.as_view(), name='request')

]