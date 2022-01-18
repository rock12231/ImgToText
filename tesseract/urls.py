from django.urls import path
from tesseract import views

urlpatterns = [
       path('', views.index, name='homepage'),
]
