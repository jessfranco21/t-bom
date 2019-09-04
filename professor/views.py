from django.shortcuts import render
from rest_framework import viewsets
from professor.models import Professor
from professor.serializers import ProfessorSerializer
# Create your views here.

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer