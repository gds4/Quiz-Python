import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# Caminho do banco de dados
DATABASE_URL = "sqlite:///app/database/meubanco.db"

# Criando o motor do banco
engine = create_engine(DATABASE_URL, echo=True)

# Criando a base declarativa para os models
Base = declarative_base()

# IMPORTANDO OS MODELS ANTES DE CRIAR AS TABELAS

from models.Questao import Questao
from models.Resposta import Resposta

# Criando a sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def criar_tabelas_banco():
    print(" Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print(" Tabelas criadas com sucesso!")


#Popula o banco de dados a partir do arquivo SQL.
def populate_database():
    
    sql_file = "app/database/populate_database.sql"

    if os.path.exists(sql_file):
        with open(sql_file, "r", encoding="utf-8") as file:
            sql_statements = file.read()

        with engine.connect() as connection:
            for statement in sql_statements.split(";"):
                if statement.strip():
                    connection.execute(text(statement))
            connection.commit()

    else:
        print(f" Arquivo {sql_file} não encontrado. O banco não foi populado.")

criar_tabelas_banco()
populate_database()
