from django.shortcuts import render
from .models import CategoryFood,Comment, Food
from .serializers import CategoryFoodSerializer,FoodSerializer,CommentSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class CategoryFoodView(viewsets.ModelViewSet):
    queryset = CategoryFood.objects.all()
    serializer_class = CategoryFoodSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class FoodView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    


