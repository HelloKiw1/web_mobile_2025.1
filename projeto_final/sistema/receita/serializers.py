from receita.models import Receita
from rest_framework import serializers

class SerializadorReceita(serializers.ModelSerializer):
    nome_nome = serializers.SerializerMethodField()
    nome_tipo = serializers.SerializerMethodField()
    nome_gosto = serializers.SerializerMethodField()    
    
    class Meta:
        model = Receita
        exclude = []

    def get_nome_nome(self, instancia):
        return instancia.get_nome_display()
    def get_nome_tipo(self, instancia):
        return instancia.get_tipo_display()
    def get_nome_gosto(self, instancia):
        return instancia.get_gosto_display()
