from dataclasses import fields
from rest_framework import serializers
from .models import Food
from drf_extra_fields.fields import Base64ImageField


class FoodSerializer(serializers.ModelSerializer):
    img = Base64ImageField(required=False)
    class Meta:
        model = Food
        fields = ('id','name','img','detail_food','published','price','slug')
