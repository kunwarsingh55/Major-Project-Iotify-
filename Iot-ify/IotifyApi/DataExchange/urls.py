from django.contrib import admin
from django.urls import path , include
from DataExchange.views import PiData,AndroidData
from . import views
# Pi send receive , Android Send Rec.
# arduino receive and send data

urlpatterns = [
    path('piData/',PiData.as_view()),
    path('androidData/',AndroidData.as_view()),
    path('handshake/', views.handShake),
]
