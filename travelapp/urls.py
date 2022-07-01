from travelproject import settings
from . import views
from django.urls import path


urlpatterns = [

    path('',views.demo,name='demo'),


]

