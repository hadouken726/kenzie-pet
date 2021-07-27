from django.urls import path
from api.views import AnimalsView


urlpatterns = [path('animals/', AnimalsView.as_view())]