from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView 
from rest_framework.response import Response

from product.serializers import ProductSerializer, CategorySerializer


from .models import Product,Category

class ProductListView(APIView):
    def get(self,request,format=None):
        products = Product.objects.all()
        serializers = ProductSerializer(products,many=True)
        return Response(serializers.data)

class ProductDetail(APIView):
    def get(self,request,id):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise Http404

class CategoryDetail(APIView):
    def get(self,request,category_slug):
        try: 
            category = Category.objects.get(slug=category_slug)
            serializers = CategorySerializer(category)
            return Response(serializers.data)
        except Category.DoesNotExist:
            raise Http404
