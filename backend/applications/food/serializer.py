from dataclasses import fields
from rest_framework import serializers
from .models import Food, Category

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id','name','img','detail_food','published','category','price')

class CategoryFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')