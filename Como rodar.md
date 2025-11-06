# Como executar os projetos (Guia rápido)

Este documento explica, passo a passo, como preparar e rodar os dois projetos do repositório no Windows (PowerShell). As instruções são pensadas para desenvolvimento local.

## Projetos

- `projeto_aula` — Carros
- `projeto_final` — Receitas

## Pré-requisitos

- Python 3.11+ (recomendado: instalador oficial)
- PostgreSQL (se for usar banco PostgreSQL) ou SQLite para testes rápidos
- PgAdmin4 (opcional) ou `psql` no PATH

---

## 1) Criar o ambiente virtual (.venv)

No PowerShell, entre na pasta do projeto desejado (ex.: `projeto_aula`) e execute:

```powershell
cd C:\Users\eduar\Documents\GitHub\web_mobile_2025.1\projeto_aula
python -m venv .venv
```

> Observação: pode usar `venv` ou outro nome em vez de `.venv`.

## 2) Ativar a `.venv`

PowerShell (recomendado):

```powershell
cd C:\Users\eduar\Documents\GitHub\web_mobile_2025.1\projeto_aula
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear execução de scripts, rode (apenas nesta sessão):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1
```

Alternativas:

- CMD:

```cmd
\.venv\Scripts\activate.bat
```

- Git Bash / WSL:

```bash
source .venv/Scripts/activate
```

---

## 3) Instalar dependências

Com o `.venv` ativado:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Se não existir `requirements.txt` no projeto, instale manualmente (ex.: `pip install django djangorestframework`).

---

## 4) Criar o banco de dados (PostgreSQL)

### Usando PgAdmin4 (GUI)

1. Abra PgAdmin4 e conecte ao servidor (Host: `127.0.0.1` / `localhost`, Port: `5432`).
2. Clique com o botão direito em `Databases` → `Create` → `Database...`.
3. Preencha:
   - Name: `sistema`
   - Owner: `postgres` (ou outro usuário)
   - Encoding: `UTF8`
4. Salve.

### Usando psql (linha de comando)

```powershell
psql -h 127.0.0.1 -U postgres -c "CREATE DATABASE sistema WITH OWNER = postgres ENCODING = 'UTF8' TEMPLATE = template0;"
```

> Ajuste usuário/senha em `settings.py` se não usar `postgres`/`postgres`.

---

## 5) Aplicar migrações e criar superuser

Entre na pasta que contém `manage.py` (ex.: `sistema`):

```powershell
cd C:\Users\eduar\Documents\GitHub\web_mobile_2025.1\projeto_aula\sistema
```

Execute:

```powershell
python manage.py makemigrations
python manage.py migrate
```

Criar superuser (interativo):

```powershell
python manage.py createsuperuser
```

Criar superuser não interativamente (PowerShell):

```powershell
$env:DJANGO_SUPERUSER_USERNAME = "admin"
$env:DJANGO_SUPERUSER_EMAIL = "admin@example.com"
$env:DJANGO_SUPERUSER_PASSWORD = "admin"
python manage.py createsuperuser --noinput
```

---

## 6) Rodar o servidor de desenvolvimento

```powershell
python manage.py runserver
```

Ou, sem ativar a venv, use:

```powershell
C:\Users\eduar\Documents\GitHub\web_mobile_2025.1\projeto_aula\.venv\Scripts\python.exe manage.py runserver
```

---

## 7) Exemplo rápido (fluxo mínimo)

```powershell
cd C:\Users\eduar\Documents\GitHub\web_mobile_2025.1\projeto_aula
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
cd sistema
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 8) Troubleshooting (erros comuns)

- "Couldn't import Django": ative o `.venv` correto ou execute com o Python do venv (`.venv\\Scripts\\python.exe`).
- UnicodeDecodeError ao conectar ao Postgres: verifique host/porta no `settings.py`, variáveis de ambiente (ex.: `PGPASSFILE`) e que `psycopg2-binary` está instalado.
- Erro de autenticação: confirme usuário/senha no Postgres e no `settings.py`.

---

## 9) Observações

- Evite manter múltiplos venvs no repositório; use `.gitignore` para ignorá-los.
- Posso gerar um script PowerShell (`setup-project.ps1`) que automatize criação do venv e instalação de deps para um dos projetos — quer que eu faça isso?
