from django.shortcuts import render
from rest_framework import viewsets
from landing.models import Aluno
from landing.serializers import AlunoSerializer
# Create your views here.

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer