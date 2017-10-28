from django.shortcuts import render, get_object_or_404, redirect
from .models import Country, Category, Material, MainComponent, MinorComponent, Product, Favorite
from .models import MainRecyclingInfomation, MinorRecyclingInfomation
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import ProductSerializer, MainComponentSerializer, MinorComponentSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

def index(request):
    components = MainComponent.objects.all()
    for comp in components:
        print(comp)
    context = {}
    return render(request, "recycleapp/index.html", context)

class ProductList(APIView):
    """
    List all products, or create a new product
    """

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # def perform_create(self, serializer):
    #     location = Location.objects.get(pk=serializer.location)
    #     print("location: {}".format(location))
    #     serializer.save(user=self.request.user, location=location)

    # def post(self, request, format=None):
    #     serializer = PlaceSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         print("place serailizer not valid")
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComponentList(APIView):
    """
    List all components
    """

    def get(self, request, format=None):
        components = MainComponent.objects.all()
        serializer = MainComponentSerializer(components, many=True)
        return Response(serializer.data)