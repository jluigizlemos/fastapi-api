# FastAPI — API de Pedidos e Autenticação

API REST desenvolvida com **Python** e **FastAPI** para gerenciamento de contas de usuários e pedidos, com autenticação segura de senhas (bcrypt) e migrações de banco de dados gerenciadas com **Alembic**.

---

## Funcionalidades

- Cadastro de usuários com senha criptografada (bcrypt)
- Verificação de e-mail duplicado antes do cadastro
- Estrutura preparada para rotas autenticadas de pedidos
- Documentação interativa automática via Swagger UI (`/docs`)
- Migrações de banco de dados com Alembic
- Configuração flexível de banco de dados via variável de ambiente

---

## Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.12+ | Linguagem |
| FastAPI | Framework web |
| SQLAlchemy | ORM (mapeamento objeto-relacional) |
| Alembic | Migrações de banco de dados |
| Passlib + bcrypt | Hash e verificação de senhas |
| Uvicorn | Servidor ASGI |
| uv | Gerenciador de dependências |

---

## Estrutura do projeto

```
.
├── main.py               # Inicialização do app e roteamento principal
├── models.py             # Modelos/entidades do banco (Usuário, Pedido, Itens)
├── auth_routes.py        # Rotas de autenticação e cadastro
├── order_routes.py       # Rotas de pedidos
├── dependencies.py       # Injeção de dependências (sessão do banco)
├── alembic/              # Configuração e migrações do banco
├── alembic.ini
├── pyproject.toml        # Dependências do projeto
└── .env.example          # Exemplo de variáveis de ambiente
```

---

## Como executar

### Pré-requisitos
- Python 3.12 ou superior
- [uv](https://docs.astral.sh/uv/)

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/jluigizlemos/fastapi-api.git
cd fastapi-api

# 2. Instale as dependências
uv sync

# 3. Configure as variáveis de ambiente
#    Crie um arquivo .env a partir do .env.example

# 4. Aplique as migrações do banco
alembic upgrade head

# 5. Suba o servidor
uv run uvicorn main:app --reload
```

Acesse:
- API: http://127.0.0.1:8000
- Documentação interativa (Swagger): http://127.0.0.1:8000/docs

---

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Health check da API |
| GET | `/auth` | Rota padrão de autenticação |
| POST | `/auth/criar_conta` | Cria uma conta de usuário (email, senha, nome) |
| GET | `/pedidos` | Rota padrão de pedidos |

---

## Exemplo de uso

Cadastrar um usuário:

```bash
curl -X POST "http://127.0.0.1:8000/auth/criar_conta" \
  -d "email=exemplo@teste.com&senha=12345&nome=Seu Nome"
```

Resposta esperada:

```json
{ "mensagem": "usuário cadastrado com sucesso" }
```

---

## Roadmap

- [ ] Implementar autenticação com JWT (login/token)
- [ ] Rotas CRUD completas de pedidos e itens
- [ ] Testes automatizados (pytest)
- [ ] Deploy em produção (Docker + nuvem)

---

## Licença

Este projeto está sob a licença MIT.
