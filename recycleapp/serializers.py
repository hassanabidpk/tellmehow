from rest_framework import serializers
from .models import Country, Category, Material, MainComponent, MinorComponent, Product, Favorite
from .models import MainRecyclingInfomation, MinorRecyclingInfomation
from django.contrib.auth.models import User
import json


class CategorySerialier(serializers.ModelSerializer):
    
    class Meta:
        model = Category

class MinorComponentSerializer(serializers.ModelSerializer):
    material = serializers.StringRelatedField()
    recyclinginfomation = serializers.SerializerMethodField()

    def get_recyclinginfomation(self, obj):
        r_info = MinorRecyclingInfomation.objects.filter(component__pk=obj.pk)
        print("minor_comp : {}".format(r_info))
        if r_info:
            return r_info[0].info
        else :
            return None

    class Meta:
        model =  MinorComponent
        fields = ('id', 'name', 'material', 'recyclinginfomation')


class MainComponentSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    material = serializers.StringRelatedField()
    recyclinginfomation = serializers.SerializerMethodField()
    minor_components = MinorComponentSerializer(read_only=True, many=True)

    def get_recyclinginfomation(self, obj):
        r_info = MainRecyclingInfomation.objects.filter(component__pk=obj.pk)
        print("main_comp : {}".format(r_info))        
        if r_info:
            return r_info[0].info
        else :
            return None

    class Meta:
        model =  MainComponent
        fields = ('id', 'name', 'category', 'material', 
                    'recyclinginfomation', 'minor_components')

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    main_component = MainComponentSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'code', 'photo', 'user', 'main_component',
                  'slug', 'updated_at', 'created_at')

class CategorySerialier(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'name', '')