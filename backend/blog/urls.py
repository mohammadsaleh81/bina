from django.urls import path
from rest_framework import routers
from .views import LawViweSet

app_name= 'blog'

router = routers.SimpleRouter()
router.register("Law",LawViweSet, basename='Law')

urlpatterns = router.urls