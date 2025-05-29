# 🌐 WEB_MOBILE_2025.1  
## 📘 Diário de Aula – Desenvolvimento Web Mobile

---

## ✅ Registro das Aulas

### **12 de março – Aula 1: Introdução à Matéria + Primeiros Arquivos**

🔹 **Conteúdo teórico apresentado:**  
[Cap. 1 – Aspectos Introdutórios](https://www.notion.so/Cap-1-Aspectos-Introd-rio-1b4ff6c3908a80d0b87dfa3a0640f179?pvs=25)

🧪 **Atividades práticas realizadas:**  
- Criação da conta no GitHub  
- Criação e clonagem do repositório `web_mobile`  
- Introdução ao VSCode e primeiros comandos Git  
- Criação dos primeiros arquivos:  

```
aula-1.html
js/funcoes.js
css/styles.css
```

---

### **26 de março – Aula 2: Conceito de Frameworks + Métodos HTTP**

🔹 **Conteúdo teórico apresentado:**  
[Cap. 2 – Frameworks](https://www.notion.so/Cap-2-Frameworks-1c2ff6c3908a80e09d83fc6ea4a625c8?pvs=21)

🧪 **Atividades práticas realizadas:**  
- Criação do arquivo `aula-2.html`  
- Explicação sobre `action` e `method` em formulários  
- Estudo dos principais verbos HTTP:  

```
POST    → Enviar dados
GET     → Receber dados
PUT     → Atualizar dados
DELETE  → Excluir dados
```

---

### **02 de abril – Aula 3: Criação de Ambiente Virtual + Gitignore**

🔹 **Conteúdo teórico apresentado:**  
- [Cap. 3 – Padrões Arquiteturais](https://www.notion.so/Cap-3-Padr-es-Arquiteturais-1c9ff6c3908a80a3b3dbed50d7400903?pvs=25)  
- [Cap. 4 – ORM](https://www.notion.so/Cap-4-ORM-1c9ff6c3908a80dbaddac08ebe1ac360?pvs=25)

🧪 **Atividades práticas realizadas:**  
- Criação do ambiente virtual com `virtualenv`  
- Ativação e desativação:  

```bash
source virtual/bin/activate
deactivate
```

- Uso do `.gitignore` para ignorar arquivos no Git:  

```bash
cat .gitignore
```

---

### **09 de abril – Aula 4: Prática com Ambiente Virtual + Introdução ao Django**

🔹 **Conteúdo teórico apresentado:**  
- [Cap. 5 – Criação do Ambiente Virtual – Prática](https://www.notion.so/Cap-5-Cria-o-do-Ambiente-Virtual-Pratica-1c9ff6c3908a80e286a6cebaf861ee48?pvs=25)  
- [Cap. 6 – Introdução ao Django](https://www.notion.so/Cap-6-1d0ff6c3908a80d88a0ff6f0e6a9bce7?pvs=25)

🧪 **Atividades práticas realizadas:**  
- Instalação do Django no ambiente virtual:  

```bash
pip install django
django-admin --version
```

- Início do projeto Django com:  

```bash
django-admin startproject nome_projeto
```

- Discussão sobre a arquitetura MTV (Model – Template – View)

---

### **16 de abril – Aula 5: Desenvolvimento com Django + Estrutura de Apps**

🔹 **Conteúdo teórico apresentado:**  
[Cap. 7 – Desenvolvimento com Django](https://www.notion.so/Cap-7-1d7ff6c3908a80a1b87ccb658588cc11?pvs=25)

🧪 **Atividades práticas realizadas:**  
- Criação de projeto e app Django  
- Comando para rodar o servidor local  
- Adicionar o App no `settings.py`  
- Diferença entre projeto e app

---

### **23 de abril – Aula 6: Migrações no Banco de Dados + CRUD no Django**

🔹 **Conteúdo teórico apresentado:**  
[Cap. 8 – Migrações, Banco de Dados, CRUD e Class-Based Views](https://www.notion.so/Cap-8-1deff6c3908a80d68ff0e0ea301a04b3?pvs=25)

🧪 **Atividades práticas realizadas:**  
- Rodar as migrações no banco de dados  
- Revisão dos métodos HTTP e códigos de status  
- Introdução às Class-Based Views e Mixins  
- Inserção e consulta de dados no Django Shell

---

### **07 de maio – Aula 7: Herança de Templates + Formulários + Views com Classe**

🔹 **Conteúdo teórico apresentado:**  
- [Cap. 9 – Herança de Templates](https://www.notion.so/Cap-9-1e5ff6c3908a806b99a8d75d68792b60?pvs=4)  
- [Cap. 10 – Views com Classe e Formulários](https://www.notion.so/Cap-10-1ecff6c3908a8010a3eccf29e941b794?pvs=4)

🧪 **Atividades práticas realizadas:**  
- Estruturação de templates com `base.html` e blocos `{% block %}`  
- Criação do `forms.py` e formulário com ModelForm  
- Implementação das views com `CreateView`  
- Adição das rotas no `urls.py`  
- Criação do template `novo.html`  
- Adição de imagens aos veículos

---

### **14 de maio – Aula 8: Restrições de Acesso + Editar e Deletar Veículos**

🔹 **Conteúdo teórico apresentado:**  
[Cap. 11 – Controle de Acesso e Funcionalidades Avançadas](https://www.notion.so/Cap-11-1f3ff6c3908a8011a838c504d157c6cc?pvs=4)

🧪 **Atividades práticas realizadas:**  
- Implementação da verificação de login (`LoginRequiredMixin`)  
- Definição da URL de login no `settings.py`  
- Criação da view `EditarVeiculos` com `UpdateView`  
- Rota para editar veículos adicionada ao `urls.py`  
- Criação de novo app `anuncio`  
- Adição de `ForeignKey` para relacionamento entre modelos  
- Melhoria no controle de acesso e nas funcionalidades CRUD

---

### **21 de maio – Aula 9: Testes no Django + TDD (Desenvolvimento Guiado por Testes)**

🔹 **Conteúdo teórico apresentado:**  
[Cap. 12 – Testes](https://www.notion.so/Cap-12-Testes-1faff6c3908a803cab2ce520cfb3c454)

🧪 **Atividades práticas realizadas:**  
- Introdução ao conceito de **TDD (Test-Driven Development)**:  
  🔸 Técnica que visa otimizar o desenvolvimento de software, reduzindo falhas no desenvolvimento e na entrega.  
  🔸 Processo cíclico:  
    1. Escreve-se um teste automatizado para uma nova funcionalidade.  
    2. Desenvolve-se o código mínimo necessário para que o teste passe.  
    3. Refatora-se o código, mantendo os testes passando.  

- **Tipos de Testes:**  
  - ✅ **Teste de Unidade (Unitário)** – ⚠️ **Tema de prova!**  
    Verifica métodos, funções ou componentes isolados.  

    Exemplo:  

    ```javascript
    function soma(a, b) {
      return a + b;
    }

    var resultado = soma(1, 2);
    expect(resultado).to.equal(3);
    ```

  - 🔸 **Teste de Integração** – Testa a interação entre módulos.  
  - 🔸 **Teste de Carga** – Verifica desempenho sob alta demanda.  
  - 🔸 **Teste de Aceitação** – Valida se o sistema atende aos requisitos.  
  - 🔸 **Teste de Segurança** – Avalia vulnerabilidades no sistema.  

- **Criação de Testes no Django:**  
Arquivo: `veiculo/tests.py`  

```python
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from veiculo.models import Veiculo

class TesteModelVeiculo(TestCase):
    def setUp(self):
        self.instancia = Veiculo(
            marca=1,
            modelo='ABCDE',
            ano=datetime.now().year,
            cor=2,
            combustivel=3,
        )

    def test_is_new(self):
        self.assertTrue(self.instancia.veiculo_novo)
        self.instancia.ano = datetime.now().year - 5
        self.assertFalse(self.instancia.veiculo_novo)
```

- **Executando os testes no Django:**  

```bash
python manage.py test
```

---

### **28 de maio – Aula 10: API REST com Django REST Framework**

🔹 **Conteúdo teórico apresentado:**  
- [Cap. 13 – APIs – Interface de Programação de Aplicações](https://www.notion.so/Cap-13-API-s-Interface-de-programa-o-de-aplica-es-13d6f8b90b2446a6a75d62e13db330cc?pvs=4)

🧪 **Atividades práticas realizadas:**  

- Instalação do Django REST Framework e CORS Headers:

```bash
pip install djangorestframework
pip install django-cors-headers
```

- Configurações em `settings.py` (ou `config.py`):

```python
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...,
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

CORS_ORIGIN_ALLOW_ALL = True
```

- Criar o serializer para o modelo Veículo (`veiculo/serializer.py`):

```python
from veiculo.models import Veiculo
from rest_framework import serializers

class SerializadorVeiculo(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        exclude = []
```

- Criar a API view para listar veículos (`veiculo/views.py`):

```python
from rest_framework.generics import ListAPIView
from veiculo.serializers import SerializadorVeiculo
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions

class APIListarVeiculos(ListAPIView):
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()
```

- Atualizar rotas em `veiculo/urls.py`:

```python
from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('api/', APIListarVeiculos.as_view(), name='api-listar-veiculos'),
    path('foto/<str:arquivo>', FotoVeiculo.as_view(), name='foto-veiculo'),
]
```

- Teste da API (usar o token do usuário autenticado):

```bash
curl http://127.0.0.1:8000/veiculo/api/ -H 'Authorization: Token SEU_TOKEN_AQUI'
```

- Verificação de funcionamento:

```bash
./manage.py check
```

---