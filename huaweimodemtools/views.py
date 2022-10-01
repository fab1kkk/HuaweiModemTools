from django.shortcuts import render
from random import seed
from random import randint
from django.http import HttpResponse, JsonResponse

import huaweimodemtools.huaweiApi
import huaweimodemtools.huaweiApiFake

# Create your views here.


def generate_random(request):
	return render(request, "form.html")

def getSignalInfo(request):
	signalInfo = huaweimodemtools.huaweiApi.getDeviceSignal()
	#signalInfo = huaweimodemtools.huaweiApiFake.getDeviceSignal()
	return JsonResponse(signalInfo);