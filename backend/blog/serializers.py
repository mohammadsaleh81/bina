import re

from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from .models import Category, Law


class CategorySrializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= ['title', 'slug']



class LawSeralizer(TaggitSerializer, serializers.ModelSerializer):
    
    def get_author(self, obj):
        return {
			"username": obj.author.username,
			"first_name": obj.author.first_name,
			"last_name": obj.author.last_name,
		}
    
    
    
    
    tags = TagListSerializerField()
    author = serializers.SerializerMethodField('get_author')
    
    category = CategorySrializer(read_only=True, many=True)


    

    class Meta:
        model = Law
        fields = '__all__'
