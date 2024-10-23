from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics


# product list
class Product_List_Api(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer



class Product_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    lookup_field='id'