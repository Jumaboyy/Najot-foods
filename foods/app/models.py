from django.db import models
from rest_framework.authtoken.admin import User


# Create your models here.

class CategoryFood(models.Model):
    name = models.CharField(max_length=100,verbose_name='Category')

    def __str__(self):
        return self.name


class Food(models.Model):
    name=models.CharField(max_length=100,verbose_name='Food name')
    price=models.IntegerField(max_length=100,verbose_name='Price')
    category=models.ForeignKey(CategoryFood,on_delete=models.CASCADE,verbose_name='Category')
    composition=models.CharField(verbose_name='Tarkibi')

    def __str__(self):
        return self.name

class Comment(models.Model):
    food=models.ForeignKey(Food,on_delete=models.CASCADE,verbose_name='Food')
    comment=models.CharField(max_length=1000,verbose_name='Comment')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Date')
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='User')

    def __str__(self):
        return self.food