from django.urls import path
from pets.views import AnimalsView


urlpatterns = [path('animals/', AnimalsView.as_view())]