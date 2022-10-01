from django.urls import path
from .views import *

urlpatterns = [
	path('',generate_random),
	path('signal-info',getSignalInfo)
]
