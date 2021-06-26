from django.urls import path, include
from .views import home, empresadata

urlpatterns = [
    path('', home, name='home'),
    path('empresadata/', empresadata, name='empresadata'),
]