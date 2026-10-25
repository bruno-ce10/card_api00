# 🚗 Cars API

API REST desenvolvida com Python, Django e Django REST Framework para gerenciamento de marcas e carros.

O projeto permite realizar operações de cadastro, consulta, atualização e exclusão de registros, além de oferecer autenticação, controle de permissões e filtros para consultas.

---

## 📌 Sobre o projeto

## 📌 Sobre o projeto

A Cars API é uma API REST desenvolvida com Python, Django e Django REST Framework para o gerenciamento de marcas e carros.

O projeto conta com uma área administrativa do Django, que permite cadastrar, consultar, editar e excluir registros de marcas e carros. Também utiliza autenticação JWT, filtros, paginação e controle de permissões para organizar o acesso aos recursos da API.

A aplicação utiliza SQLite para armazenar os dados.

## 🚀 Funcionalidades

- 🏷️ Cadastro e gerenciamento de marcas
- 🚘 Cadastro e gerenciamento de carros
- 🔐 Autenticação com tokens JWT
- 🛡️ Controle de permissões de acesso
- 🔎 Filtragem de registros
- 📄 Paginação de resultados
- 💾 Armazenamento de dados com SQLite
- ⚙️ Área administrativa para gerenciamento dos registros

## 🛠️ Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Git
- GitHub

---

## 📂 Estrutura do projeto

```text
cars_api/
├── cars/
│   ├── migrations/
│   ├── admin.py
│   ├── filters.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## ▶️ Como executar o projeto

### Pré-requisitos

- Python compatível com a versão do Django utilizada
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/bruno-ce10/card_api00

### 2. Acesse a pasta do projeto

```bash
cd cars_api00
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. Criar um usuário administrador

Para acessar a área administrativa do Django, execute:

```bash
python manage.py createsuperuser
```

Preencha as informações solicitadas no terminal para criar o usuário.

### 8. Iniciar o servidor

```bash
python manage.py runserver
```

### 9. Acessar a área administrativa

Abra o endereço no navegador:

http://127.0.0.1:8000/admin/

Entre com o usuário e a senha criados anteriormente.

Na área administrativa, é possível gerenciar os registros disponibilizados pelo projeto, como carros e marcas.

**Observação:** o servidor de desenvolvimento deve permanecer em execução enquanto a aplicação estiver sendo utilizada localmente.


A API estará disponível localmente em:

`http://127.0.0.1:8000/api/v1/`

---

## 🔗 Principais endpoints

| Endpoint | Descrição |
|---|---|
| `/api/v1/brands/` | Listagem e gerenciamento de marcas |
| `/api/v1/cars/` | Listagem e gerenciamento de carros |
| `/api/v1/token/` | Obtenção de tokens JWT |
| `/api/v1/token/refresh/` | Renovação do token de acesso |
| `/admin/` | Área administrativa do Django |

As operações disponíveis dependem da autenticação e das permissões configuradas.

---

## 🎯 Objetivos de aprendizagem

Este projeto permite praticar:

- Desenvolvimento de APIs REST
- Criação de modelos e relacionamentos
- Serialização de dados
- Criação de rotas e endpoints
- Autenticação e autorização
- Filtros e paginação
- Integração com banco de dados
- Organização de projetos Python

---

## 👨‍💻 Desenvolvedor

**Bruno Cé**

Estudante de Análise e Desenvolvimento de Sistemas, com interesse em desenvolvimento de software e aplicações web.

---

⭐ Explore o repositório para conhecer a implementação da API.
