from django.urls import path
from .views import FoodList, FoodDetailView, ShowImageField

app_name = 'food'

urlpatterns = [
    path('food/', FoodList.as_view()),
    path('detail_food/<food_slug>/', FoodDetailView.as_view()),
    path('imgJson/', ShowImageField.as_view(), name= 'IMGJson'),
]
