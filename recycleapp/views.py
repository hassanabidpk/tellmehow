from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Country, Category, Material, MainComponent, MinorComponent, Product, Favorite
from .models import MainRecyclingInfomation, MinorRecyclingInfomation
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import ProductSerializer, MainComponentSerializer, MinorComponentSerializer, CategorySerialier
from .serializers import MaterialSerialier
from rest_framework import mixins
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
import json
from django.core import serializers

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

class ProductDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ProductDetailFromCode(APIView):
    
    def get_object(self, code):
        try:
            return Product.objects.get(code=code)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, code, format=None):
        product = self.get_object(code)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ComponentList(APIView):
    """
    List all components
    """

    def get(self, request, format=None):
        components = MainComponent.objects.all()
        serializer = MainComponentSerializer(components, many=True)
        return Response(serializer.data)

class CategoryList(APIView):
    """
    List all categories
    """

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerialier(categories, many=True)
        return Response(serializer.data)

class ComponentDetail(APIView):
    
    def get_object(self, pk):
        try:
            return MainComponent.objects.get(pk=pk)
        except MainComponent.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        component = self.get_object(pk)
        serializer = MainComponentSerializer(component)
        return Response(serializer.data)

class MaterialList(APIView):

    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        components = MainComponent.objects.filter(category=category)
        response_data = {}
        materials = []
        for component in components:
            materials.append(component.material)
        serializer = MainComponentSerializer(components, many=True)
        serializer_mat = MaterialSerialier(materials, many=True)
        response_data["components"] = serializer.data
        response_data["materials"] = serializer_mat.data
        return HttpResponse(JsonResponse(response_data), content_type="application/json")

class ComponentDetailFromMaterial(APIView):

    def get(self, request, pk):
        material = Material.objects.get(pk=pk)
        category_id = request.GET['category']
        if category_id:
            category = Category.objects.get(pk=category_id)
        component_query = MainComponent.objects.filter(material=material)
        print("type : {}".format(type(component_query)))
        response_data = {}
        components = []
        result_component = None
        if component_query:
            for comp in component_query:
                print("type comp : {}".format(type(comp)))
                if comp.category.pk == category.pk:
                    result_component = comp
                components.append(comp)
            serializer = MainComponentSerializer(result_component)
            response_data["component"] = serializer.data
        else :
            response_data["component"] = None
        return HttpResponse(JsonResponse(response_data), content_type="application/json")

