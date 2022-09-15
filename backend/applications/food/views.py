from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Food
from .serializer import FoodSerializer

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
    

