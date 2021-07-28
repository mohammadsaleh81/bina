from re import L
from django.db import models
from django.db.models.query import QuerySet
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Law, Category
from .serializers import LawSeralizer, CategorySrializer


class LawViweSet(ModelViewSet):
    serializer_class = LawSeralizer
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Law.objects.all()
        
        else:
            return Law.objects.filter(author=self.request.user)
    
    filterset_fields = ["status", "author"]
    ordering_fields = ["created","status"]
    search_fields = [
        'title',
        'description',
        'tags__name'
    ]

@api_view(['GET'])
def Taglist(request, tag):
    
    tags = Law.objects.filter(tags__name=tag)
    serializer = LawSeralizer(tags, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Categorylist(request, category):
    
    category = Law.objects.filter(category__slug=category)
    serializer = LawSeralizer(category, many=True)
    return Response(serializer.data)



