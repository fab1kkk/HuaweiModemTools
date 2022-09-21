from django.urls import path
from .views import *

urlpatterns = [
	path('',generate_random),
	path('url',generate_number),
]
