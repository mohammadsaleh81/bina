from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Law
from .serializers import LawSeralizer

class LawViweSet(ModelViewSet):
    serializer_class = LawSeralizer
    queryset = Law.objects.all()
    filterset_fields = ["status", "author"]
    ordering_fields = ["created","status"]
    search_fields = [
        'title',
        'description'
    ]
