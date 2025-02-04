from sqlalchemy import Column, Integer, String
from database.database import Base  

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, email={self.email})"
