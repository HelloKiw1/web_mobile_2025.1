from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from receita.models import Receita
from django.core.files.uploadedfile import SimpleUploadedFile


class ReceitaModelTest(TestCase):
    def setUp(self):
        # Cria uma instância de Receita para testes
        self.receita = Receita.objects.create(
            nome='Bolo de Chocolate',
            tipo=1,  # considerando que 1 é um tipo válido em OPCOES_TIPO
            gosto=2,  # exemplo válido em OPCOES_GOSTO
            tempo_preparo=timedelta(minutes=45),
            porcoes=8,
            dificuldade=1,  # exemplo válido em OPCOES_DIFICULDADE
            ingredientes='Farinha, Açúcar, Chocolate em pó, Ovos, Leite',
            receita='Misture os ingredientes e asse por 40 minutos.'
        )

    def test_str_representation(self):
        # Verifica se __str__ retorna o nome da receita
        self.assertEqual(str(self.receita), 'Bolo de Chocolate')

    def test_str_representation_sem_nome(self):
        # Se não tiver nome, retorna 'Receita sem nome'
        receita_sem_nome = Receita.objects.create()
        self.assertEqual(str(receita_sem_nome), 'Receita sem nome')

    def test_tempo_preparo_duration(self):
        # Verifica se tempo_preparo está armazenado corretamente como timedelta
        self.assertEqual(self.receita.tempo_preparo, timedelta(minutes=45))

    # Exemplo de método que calcula se receita é nova (você pode adaptar conforme sua model)
    def test_receita_novo_property(self):
        # Vamos supor que receita_novo seja True para receitas do ano atual
        current_year = datetime.now().year

        # Ajustar o modelo se tiver o campo ano, aqui só exemplo
        self.receita.ano = current_year
        self.receita.save()

        # Supondo que o modelo tenha receita_novo como property
        # Se não tiver, remova ou implemente na model
        if hasattr(self.receita, 'receita_novo'):
            self.assertTrue(self.receita.receita_novo)
            self.receita.ano = current_year - 10
            self.receita.save()
            self.assertFalse(self.receita.receita_novo)


class ReceitaListViewTest(TestCase):
    def setUp(self):
        # Cria usuário e força login
        self.user = User.objects.create_user(username='user_test', password='senha123')
        self.client = Client()
        self.client.login(username='user_test', password='senha123')

        # Cria algumas receitas para teste
        Receita.objects.create(nome='Receita 1', tipo=1)
        Receita.objects.create(nome='Receita 2', tipo=2)

        # URL da view listagem
        self.url = reverse('listar-receita')

    def test_listagem_status_code(self):
        # Testa se a página carrega com sucesso (HTTP 200)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_listagem_contem_receitas(self):
        # Verifica se a view retorna as receitas no contexto
        response = self.client.get(self.url)
        receitas = response.context.get('receitas')
        self.assertIsNotNone(receitas)
        self.assertEqual(len(receitas), 2)

    def test_listagem_requer_login(self):
        # Testa se o acesso sem login redireciona para página de login
        self.client.logout()
        response = self.client.get(self.url)
        self.assertNotEqual(response.status_code, 200)
        self.assertIn('/login', response.url)  # supondo que redireciona para /login/


class ReceitaCreateFormTest(TestCase):
    def test_form_valido(self):
        from receita.forms import ReceitaForm

        data = {
            'nome': 'Test Receita',
            'tipo': 1,
            'gosto': 1,
            'tempo_preparo': '00:30:00',  # formato hh:mm:ss para DurationField
            'porcoes': 4,
            'dificuldade': 2,
            'ingredientes': 'Ingredientes diversos',
            'receita': 'Modo de preparo detalhado',
        }

        form = ReceitaForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalido_sem_nome(self):
        from receita.forms import ReceitaForm

        data = {
            'tipo': 1,
            'gosto': 1,
        }
        form = ReceitaForm(data=data)
        self.assertFalse(form.is_valid())


class ReceitaFotoUploadTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user_foto', password='senha123')
        self.client = Client()
        self.client.login(username='user_foto', password='senha123')

    def test_upload_foto_receita(self):
        with open('receita/tests/test_image.jpg', 'wb') as f:
            f.write(b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b')
        with open('receita/tests/test_image.jpg', 'rb') as image:
            foto = SimpleUploadedFile('test_image.jpg', image.read(), content_type='image/jpeg')
            receita = Receita.objects.create(
                nome='Receita com Foto',
                tipo=1,
                foto=foto,
            )
            self.assertTrue(receita.foto.name.endswith('test_image.jpg'))
