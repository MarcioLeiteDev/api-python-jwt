## 🛸 API Python JWT 🛸
🚀 Uma API simples de autenticação JWT com Python e FastAPI.

## ✨ Funcionalidades
🔐 Autenticação JWT
📋 Cadastro e login de usuários
🛠️ Proteção de rotas com middleware
📂 Persistência de dados com PostgreSQL
📦 Instalação
## Clone este repositório:
```bash
git clone https://github.com/MarcioLeiteDev/api-python-jwt.git
cd api-python-jwt
```

## 🛠️ Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```
## 📦 Instale as dependências:

```bash
pip install -r requirements.txt
```
## 🚀 Executando a API
Configure as variáveis de ambiente no arquivo .env.
Inicie o servidor:
```bash
uvicorn main:app --reload
```

🔑 Endpoints Principais
Método	Endpoint	Descrição
POST	/token	Gera um token JWT
GET	/users/me	Retorna dados do usuário autenticado

## 🌌 Tecnologias
🐍 Python 3
⚡ FastAPI
🛢️ PostgreSQL
🔑 JWT
🎭 Contribuindo
Let's Go 🚀