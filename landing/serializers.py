from rest_framework import serializers 
from landing.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields =('nome', 'idade', 'email',)