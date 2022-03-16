from django.urls import include,path
from .views import main
urlpatterns = [
    path("", main)
]