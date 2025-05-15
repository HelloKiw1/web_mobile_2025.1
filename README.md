
# 🌐 WEB_MOBILE_2025.1  
## 📘 Diário de Aula – Desenvolvimento Web Mobile

---

### **12 de março – Aula 1: Introdução à Matéria + Primeiros Arquivos**

🔹 Conteúdo teórico apresentado:  
[Cap. 1 – Aspectos Introdutórios](https://www.notion.so/Cap-1-Aspectos-Introdut-rio-1b4ff6c3908a80d0b87dfa3a0640f179?pvs=25)

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

🔹 Conteúdo teórico apresentado:  
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

🔹 Conteúdo teórico apresentado:  
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

🔹 Conteúdo teórico apresentado:  
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

🔹 Conteúdo teórico apresentado:  
[Cap. 7 – Desenvolvimento com Django](https://www.notion.so/Cap-7-1d7ff6c3908a80a1b87ccb658588cc11?pvs=25)

🧪 **Atividades práticas realizadas:**
- Comando para criar um projeto Django:
  ```bash
  django-admin startproject nome_projeto
  ```
- Criação de um App com:
  ```bash
  python manage.py startapp nome_app
  ```
- Rodar o servidor local:
  ```bash
  python manage.py runserver
  ```
- Adicionar o App no `settings.py` (em `INSTALLED_APPS`)
- Diferença entre projeto e app no Django

- ---

### **23 de abril – Aula 6: Migrações no Banco de Dados + CRUD no Django**

🔹 **Conteúdo teórico apresentado:**  
[Cap. 8 – Migrações, Banco de Dados, CRUD e Class-Based Views](https://www.notion.so/Cap-8-1deff6c3908a80d68ff0e0ea301a04b3?pvs=25)

🧪 **Atividades práticas realizadas:**

- **Rodar as migrações no banco de dados:**
  ```bash
  python manage.py check
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Revisão dos Métodos HTTP**:
  ```
  POST   → Create (Criar)
  GET    → Read (Ler)
  PUT    → Update (Atualizar)
  DELETE → Delete (Excluir)
  ```

- **HTTP Status Codes principais**:
  - **2xx – Success**  
    200 OK
  - **3xx – Redirection**  
    301 Permanent Redirect | 302 Temporary Redirect | 304 Not Modified
  - **4xx – Client Error**  
    401 Unauthorized | 403 Forbidden | 404 Not Found | 405 Method Not Allowed
  - **5xx – Server Error**  
    501 Not Implemented | 502 Bad Gateway | 503 Service Unavailable | 504 Gateway Timeout

- **Introdução às Class-Based Views (CBVs)**:
  - As **CBVs** organizam a lógica de exibição (views) através de classes ao invés de funções, trazendo maior reaproveitamento de código e flexibilidade na construção das aplicações.

- **Utilizando Mixins em Views**:
  - Um **Mixin** é uma classe que adiciona funcionalidades específicas a uma outra classe através de herança múltipla.  
  - Em Django, usamos mixins para adicionar métodos reutilizáveis às views sem repetir código.

- **CRUD (Create, Read, Update, Delete)**:
  - Conjunto de operações básicas para gerenciar dados em sistemas.
    - **Create** → Criar um novo registro
    - **Read** → Consultar dados
    - **Update** → Atualizar dados existentes
    - **Delete** → Excluir registros

- **Na prática – Inserindo dados no banco de dados via Django Shell**:
  
  🔹 Acessando o shell:
  ```bash
  python manage.py shell
  ```

  🔹 Criando e salvando um novo objeto manualmente:
  ```python
  from veiculo.models import Veiculo
  
  primeiro = Veiculo()
  primeiro.marca = 1
  primeiro.modelo = 'A8'
  primeiro.ano = 2022
  primeiro.cor = 2
  primeiro.combustivel = 3
  primeiro.save()
  ```

  🔹 Criando um objeto de forma direta:
  ```python
  segundo = Veiculo(marca=4, modelo='F7', ano=2020, cor=6, combustivel=2)
  segundo.save()
  ```

  🔹 Consultando informações:
  - Contar o número de veículos cadastrados:
    ```python
    Veiculo.objects.all().count()
    ```
  - Filtrar veículos por marca:
    ```python
    Veiculo.objects.filter(marca=1).count()
    ```

Ultima aula: 
07 de mai

Explicou herança
Add block base no projeto_sala:
Add um botão para editar o veiculo
  Add Novo Veiculo
  Add Imagem
_____

14 de mai

Add Requerimento de Login
Add uma fucionalidade de add veiculos novos