# 🌐 Aplicação Web Django - Projeto Final ASII

Este projeto é uma aplicação web desenvolvida em Django, servindo como projeto final para a UC de ASII. A aplicação é containerizada com Docker e suporta dois modos de base de dados: SQLite para desenvolvimento local e MySQL para ambiente de produção via Docker.

---

## 🚀 Funcionalidades

* **Aplicação Web Django:** Interface web completa com templates HTML organizados na pasta `templates/`.
* **Módulo Principal (`core`):** App Django central com models, views e URLs da aplicação.
* **Configuração por Ambiente:** Suporte a variáveis de ambiente via `.env` (usando `python-dotenv`), permitindo configuração flexível entre desenvolvimento e produção.
* **Painel de Administração:** Gestão de conteúdos através do Django Admin.
* **Base de Dados Dual:** SQLite para desenvolvimento local e MySQL 8.0 em produção (Docker).

---

## 📋 Requisitos do Trabalho

* Repositório Git local e remoto (GitHub).
* Histórico de desenvolvimento com commits documentados.
* Aplicação Django funcional com templates HTML.
* Suporte a variáveis de ambiente via ficheiro `.env`.
* Containerização completa com Docker e Docker Compose.
* Suporte a MySQL como base de dados de produção.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10**
* **Django >= 4.2** (Framework Web)
* **SQLite** (Base de dados local / desenvolvimento)
* **MySQL 8.0** (Base de dados de produção via Docker)
* **Docker & Docker Compose** (Containerização)
* **python-dotenv** (Gestão de variáveis de ambiente)
* **pymysql + cryptography** (Conector MySQL para Python)
* **Git & GitHub** (Controlo de versões)

---

## 🔧 Como instalar e correr o projeto

### ▶️ Opção 1 — Localmente (sem Docker)

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/6kz/ASII-ProjetoFinal.git
   cd ASII-ProjetoFinal
   ```

2. **Criar e ativar o ambiente virtual:**
   ```bash
   python -m venv venv
   ```
   venv\Scripts\activate
   ```

3. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar as variáveis de ambiente:**
   ```bash
   cp .env.example .env
   # Edita o ficheiro .env com as tuas configurações
   ```

5. **Executar as migrações (configurar a base de dados):**
   ```bash
   python manage.py migrate
   ```

6. **Criar um superutilizador (para aceder ao Admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

8. **Aceder no browser:**
   * Website: http://127.0.0.1:8000/
   * Administração: http://127.0.0.1:8000/admin

---

### 🐳 Opção 2 — Com Docker Compose (recomendado para produção)

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/6kz/ASII-ProjetoFinal.git
   cd ASII-ProjetoFinal
   ```

2. **Construir e iniciar os containers:**
   ```bash
   docker compose up --build
   ```
   Isto irá levantar dois serviços:
   * `db` — MySQL 8.0 na porta `3306`
   * `web` — Aplicação Django na porta `8000`

3. **Aceder no browser:**
   * Website: http://localhost:8000/
   * Administração: http://localhost:8000/admin


---

## 📁 Estrutura do Projeto

```
ASII-ProjetoFinal/
├── core/               # App principal Django (models, views, urls)
├── setup/              # Configurações do projeto Django (settings, wsgi, asgi)
├── templates/          # Templates HTML da aplicação
├── manage.py           # Utilitário de gestão Django
├── requirements.txt    # Dependências Python
├── Dockerfile          # Imagem Docker da aplicação
├── docker-compose.yml  # Orquestração de containers (Django + MySQL)
└── .env.example        # Exemplo de variáveis de ambiente
```

---

## 👥 Autores
Tomás Matos 2025125
Gonçalo Castro 2025079
Projeto Final para a UC de ASII — Maio 2026
