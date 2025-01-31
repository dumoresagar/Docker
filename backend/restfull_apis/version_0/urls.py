from django.urls import path, include
from .authentication import urls as authentication_urls
from .users import urls as users_urls

app_name = "v0"

urlpatterns = [
    path("authentication/", include(authentication_urls), name='authentication'),
    path("users/", include(users_urls), name='users'),
  
]
