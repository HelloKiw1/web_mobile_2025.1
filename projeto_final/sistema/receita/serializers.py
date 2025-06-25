from receita.models import Receita
from rest_framework import serializers

class SerializadorReceita(serializers.ModelSerializer):
    nome_nome = serializers.SerializerMethodField()
    nome_porcoes = serializers.SerializerMethodField()
    nome_gosto = serializers.SerializerMethodField()
    nome_dificuldade = serializers.SerializerMethodField()  # Adicionado para dificuldade
    
    class Meta:
        model = Receita
        exclude = []

    def get_nome_nome(self, instancia):
        return instancia.nome

    def get_nome_porcoes(self, instancia):
        return instancia.nome

    def get_nome_gosto(self, instancia):
        return instancia.get_gosto_display()

    def get_nome_dificuldade(self, instancia):
        return instancia.get_dificuldade_display()
