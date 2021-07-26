from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import LawViweSet, Taglist, Categorylist

app_name= 'blog'

router = routers.SimpleRouter()
router.register("Law",LawViweSet, basename='Law')

urlpatterns = [
    path('', include(router.urls)),
    path('tag/<str:tag>/', Taglist),
    path('category/<str:category>/', Categorylist)
]
