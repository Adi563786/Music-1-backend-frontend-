from django.urls import path
from .services import ToggleFollow
from rest_framework.views import APIView

urlpatterns = [
    path('toggle_follows/',ToggleFollow.as_view(),name='togglefollow')
]

