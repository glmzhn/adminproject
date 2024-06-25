from rest_framework import generics
from .models import ItemCategory, Item
from .serializers import ItemCategorySerializer, ItemSerializer


class ItemCategoryList(generics.ListAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer


class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
