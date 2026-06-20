from django.shortcuts import render
from .models import Tarea
from rest_framework import viewsets
from .serializers import TareaSerializer
# Create your views here.


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    

