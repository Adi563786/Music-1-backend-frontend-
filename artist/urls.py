from django.urls import path
from .views import artist_update_view

urlpatterns = [
    path('update/',artist_update_view,name='artist_update')
]
