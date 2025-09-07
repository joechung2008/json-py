from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/parse", views.parse_json, name="parse_json"),
]
