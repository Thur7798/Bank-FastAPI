# 🏦 Bank FastAPI

Microserviço de transações bancárias desenvolvido com **FastAPI**, **SQLAlchemy** e **SQLite**. Permite criar contas, realizar depósitos e saques, e consultar transações com autenticação JWT.

## 🚀 Deploy

A API está disponível em: **https://bank-fastapi-bm7p.onrender.com**

Acesse a documentação interativa em: **https://bank-fastapi-bm7p.onrender.com/docs**

---

## 🛠️ Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/) — framework web assíncrono
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM e mapeamento de tabelas
- [databases](https://www.encode.io/databases/) — queries assíncronas
- [aiosqlite](https://github.com/omnilib/aiosqlite) — driver assíncrono para SQLite
- [PyJWT](https://pyjwt.readthedocs.io/) — autenticação via JWT
- [Pydantic](https://docs.pydantic.dev/) — validação de dados
- [Poetry](https://python-poetry.org/) — gerenciamento de dependências

---

## 📋 Endpoints

### Auth
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/auth/login` | Gera um token JWT |

### Accounts
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/accounts/` | Lista todas as contas |
| POST | `/accounts/` | Cria uma nova conta |
| GET | `/accounts/{id}/transactions` | Lista transações de uma conta |

### Transactions
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/transactions/` | Realiza depósito ou saque |

---

## ⚙️ Como rodar localmente

### Pré-requisitos

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Thur7798/Bank-FastAPI.git
cd Bank-FastAPI

# Instale as dependências
poetry install
```

### Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=sqlite:///./banco.db
ENVIRONMENT=development
```

### Executando

```bash
poetry run uvicorn src.main:app --reload
```

Acesse em: http://127.0.0.1:8000/docs

---

## 🔐 Autenticação

A API utiliza JWT Bearer Token. Para acessar as rotas protegidas:

1. Faça um `POST /auth/login` com o `user_id`
2. Copie o `access_token` retornado
3. Clique em **Authorize** no Swagger e cole o token

---

## 📁 Estrutura do Projeto

```
src/
├── controllers/     # Rotas da aplicação
├── services/        # Regras de negócio
├── models/          # Tabelas do banco de dados
├── schemas/         # Validação de entrada/saída
├── config.py        # Configurações via .env
├── database.py      # Conexão com o banco
├── security.py      # JWT e autenticação
└── main.py          # Inicialização da aplicação
```

---

## 📌 Observações

- O saldo da conta não pode ficar negativo — saques acima do saldo retornam erro `409 Conflict`
- Todas as rotas exceto `/auth/login` requerem autenticação
