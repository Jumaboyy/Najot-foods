from django.urls import path
from views import CommentView,FoodView,CategoryFoodView
from rest_framework import routers
router= routers.SimpleRouter()
router.register('foods',FoodView)
router.register('categories',CategoryFoodView)
router.register('comments',CommentView)

urlpatterns = router.urls

