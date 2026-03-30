from django.urls import path
from .services import SearchView
from .views import SearchArtistView
urlpatterns = [
    path('search/',SearchView.as_view(),name='search'),
    path('search/artist/',SearchArtistView,name='searchArtist')
]
