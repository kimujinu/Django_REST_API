from django.urls import path,include
from .views import helloAPI,randomReturn

urlpatterns = [
    path("hello/",helloAPI),
    path("<int:id>",randomReturn)
]