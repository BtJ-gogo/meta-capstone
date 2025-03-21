from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import generics

from .models import Menu
from .serializers import MenuSerializer

# Create your views here.
def index(request):
    return render(request, "index.html", {})


# API views
class MenuItemsView(generics.ListCreateView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer