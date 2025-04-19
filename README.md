
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