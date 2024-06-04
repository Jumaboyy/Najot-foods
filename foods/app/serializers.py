from rest_framework import serializers

from .models import CategoryFood,Food,Comment

class CategoryFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryFood
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
