from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///meubanco.db"

# Criando o motor do banco
engine = create_engine(DATABASE_URL, echo=True)

# Criando a sessão do banco
SessionLocal = sessionmaker(bind=engine)

# Base para os models
Base = declarative_base()

# Função para obter a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
