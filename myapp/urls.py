from django.urls import path
from .views import ItemCategoryList, ItemList

urlpatterns = [
    path('api/v1/categories/', ItemCategoryList.as_view()),
    path('api/v1/items/', ItemList.as_view()),
]
