from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Food
from .serializer import FoodSerializer
from rest_framework.parsers import JSONParser

# Create your views here.
class FoodList(APIView):
    def get(self, request, *args, **kwargs):
        list_Food = Food.objects.all()
        
        serializerFood = FoodSerializer(list_Food,many=True)
        return Response(serializerFood.data)

class FoodDetailView(APIView):
    def get(self, request, food_slug , *args, **kwargs):
        food = get_object_or_404(Food, slug= food_slug)
        serializer = FoodSerializer(food)
        return Response(serializer.data)
    
class ShowImageField(APIView):
    def get(self, request, *args):
        print(str(self.parser_classes))
        return Response({'parsers':' '.join(map(str,self.parser_classes))}, status = 204)

    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            archivo = validated_data['img']
            archivo.name = 'mi_foto.jpg'
            validated_data['img'] = archivo
            # Convertir y guardar el modelo
            imgShow = Food(**validated_data)
            imgShow.save()

            serializer_response = FoodSerializer(imgShow)

            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)