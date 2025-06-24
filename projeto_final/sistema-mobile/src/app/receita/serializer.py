from receita.models import Receita
from rest_framework import serializers

class SerializadorReceita(serializers.ModelSerializer):
    class Meta:
        model = Receita
        exclude = []
