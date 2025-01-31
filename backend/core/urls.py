from django.urls import path, include
from .views import (HomePageView,)


app_name = "core"


urlpatterns = [
    path('', HomePageView.as_view(), name='core-home-page'),
]