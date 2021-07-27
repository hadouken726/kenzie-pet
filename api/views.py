from django.core.exceptions import ObjectDoesNotExist
from api.models import Animal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import AnimalSerializer


class AnimalsView(APIView):


    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, animal_id=None):
        if not animal_id:
            animals = Animal.objects.all()
            serializer = AnimalSerializer(animals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            animal_to_get = Animal.objects.get(id=animal_id)
            serializer = AnimalSerializer(animal_to_get)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'message': 'Invalid animal_id'}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, animal_id):
        try:
            animal_to_delete = Animal.objects.get(id=animal_id)
            animal_to_delete.delete()
            return Response('', status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({'message': 'Invalid animal_id'}, status=status.HTTP_404_NOT_FOUND)

