import re
from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from .models import Law

class LawSeralizer(TaggitSerializer, serializers.ModelSerializer):
    def get_author(self, obj):
        return {
			"username": obj.author.username,
			"first_name": obj.author.first_name,
			"last_name": obj.author.last_name,
		}
    
    def safe_discription(self, obj):
        text = obj.description
        clean = re.compile('<.*?>')
        return re.sub(clean, '',text)

    
    


    tags = TagListSerializerField()
    author = serializers.SerializerMethodField('get_author')
    description = serializers.SerializerMethodField('safe_discription')
    

    class Meta:
        model = Law
        fields = '__all__'
