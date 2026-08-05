from fastapi import APIRouter, Depends
from models import Usuario, db
from sqlalchemy.orm import sessionmaker
from dependencies import pegar_sessao
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}


@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session=Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return {"mensagem": "Já existe um usuário com esse email"} 
    else: 
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome, email, senha_criptografada)
        session.add(novo_usuario)
        session.commit()

    
    return {"mensagem": "usuário cadastrado com sucesso"}