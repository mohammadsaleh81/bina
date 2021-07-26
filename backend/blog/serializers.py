from rest_framework import serializers
from .models import Law

class LawSeralizer(serializers.ModelSerializer):
    def get_author(self, obj):
        return {
			"username": obj.author.username,
			"first_name": obj.author.first_name,
			"last_name": obj.author.last_name,
		}
    
    
    author = serializers.SerializerMethodField('get_author')
    class Meta:
        model = Law
        fields = '__all__'
