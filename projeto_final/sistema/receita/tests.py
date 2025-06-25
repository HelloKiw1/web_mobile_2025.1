from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from receita.models import Receita
from django.core.files.uploadedfile import SimpleUploadedFile
from receita.forms import FormularioReceita

class ReceitaModelTest(TestCase):
    """ Testes para o modelo Receita """
    def setUp(self): # Configura o ambiente de teste
        self.receita = Receita.objects.create(
            nome='Bolo de Chocolate',
            tipo=1,  
            gosto=2,  
            tempo_preparo=timedelta(minutes=45),
            porcoes=8,
            dificuldade=1,  
            ingredientes='Farinha, Açúcar, Chocolate em pó, Ovos, Leite',
            receita='Misture os ingredientes e asse por 40 minutos.'
        )

    def test_str_representation(self):  # Verifica a representação em string do modelo Receita
        self.assertEqual(str(self.receita), 'Bolo de Chocolate')

    def test_str_representation_sem_nome(self): # Verifica a representação em string quando o nome está vazio
        receita_sem_nome = Receita.objects.create()
        self.assertEqual(str(receita_sem_nome), 'Receita sem nome')

    def test_tempo_preparo_duration(self): # Verifica se o tempo de preparo é armazenado corretamente como um objeto timedelta
        self.assertEqual(self.receita.tempo_preparo, timedelta(minutes=45))

    def test_receita_novo_property(self): # Verifica a propriedade receita_novo, que deve ser True se o ano for o atual
        current_year = datetime.now().year

        self.receita.ano = current_year
        self.receita.save()

        if hasattr(self.receita, 'receita_novo'):
            self.assertTrue(self.receita.receita_novo)
            self.receita.ano = current_year - 10
            self.receita.save()
            self.assertFalse(self.receita.receita_novo)


class ReceitaListViewTest(TestCase): # Testes para a view de listagem de receitas
    def setUp(self): # Configura o ambiente de teste
        self.user = User.objects.create_user(username='user_test', password='senha123')
        self.client = Client()
        self.client.login(username='user_test', password='senha123')

        Receita.objects.create(nome='Receita 1', tipo=1)
        Receita.objects.create(nome='Receita 2', tipo=2)

        self.url = reverse('listar-receita')

    def test_listagem_status_code(self): # Verifica se a listagem de receitas retorna o status 200
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_listagem_contem_receitas(self): # Verifica se a listagem de receitas contém as receitas criadas
        response = self.client.get(self.url)
        receitas = response.context.get('receitas')
        self.assertIsNotNone(receitas)
        self.assertEqual(len(receitas), 2)

    def test_listagem_requer_login(self): # Verifica se a listagem de receitas requer login
        self.client.logout()
        response = self.client.get(self.url)
        self.assertNotEqual(response.status_code, 200)
        self.assertIn('/login', response.url)  


class ReceitaCreateFormTest(TestCase): # Testes para o formulário de criação de receitas
    def test_form_valido(self): # Verifica se o formulário de criação de receitas é válido com dados corretos
        from receita.forms import FormularioReceita

        data = {
            'nome': 'Test Receita',
            'tipo': 1,
            'gosto': 1,
            'tempo_preparo': '00:30:00',
            'porcoes': 4,
            'dificuldade': 2,
            'ingredientes': 'Ingredientes diversos',
            'receita': 'Modo de preparo detalhado',
        }

        form = FormularioReceita(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalido_sem_nome(self): # Verifica se o formulário de criação de receitas é inválido sem o campo nome
        from receita.forms import FormularioReceita

        data = {
            'tipo': 1,
            'gosto': 1,
        }
        form = FormularioReceita(data=data)
        self.assertFalse(form.is_valid())
