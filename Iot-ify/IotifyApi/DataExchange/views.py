from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from . models import parking


# Send/Receive 
class PiData(View):

    # Return Last Parking Situation To Pi
    def get(self, request):
        latestParkingData = parking.objects.last()
        response = {
                    'spot_1': latestParkingData.spot_1,
                    'spot_2': latestParkingData.spot_2,
                    'spot_3': latestParkingData.spot_3,
                    }
        return JsonResponse(response, safe=False)


    def post(self, request):

        s1 = str(request.POST['Spot_1'])
        s2 = str(request.POST['Spot_2'])
        s3 = str(request.POST['Spot_3'])

        parkingDataUpdate = parking(spot_1=s1, spot_2=s2, spot_3=s3)
        parkingDataUpdate.save()

        response = {'message': 'Parking Data Received'}
        return JsonResponse(response, safe=False)


class AndroidData(View):

    # Return Last Parking Situation To Pi
    def get(self, request):
        latestParkingData = parking.objects.last()
        response = {
                    'spot_1': latestParkingData.spot_1,
                    'spot_2': latestParkingData.spot_2,
                    'spot_3': latestParkingData.spot_3,
                    }
        return JsonResponse(response, safe=False)



    def post(self, request):

        s1 = str(request.POST['Spot_1'])
        s2 = str(request.POST['Spot_2'])
        s3 = str(request.POST['Spot_3'])

        parkingDataUpdate = parking(spot_1=s1, spot_2=s2, spot_3=s3)
        parkingDataUpdate.save()

        response = {'message': 'Parking Data Received'}
        return JsonResponse(response, safe=False)


def handShake(request):
    response = {'message' : 'OK'}
    return JsonResponse(response,safe=False)