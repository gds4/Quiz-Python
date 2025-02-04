from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.database import Base


class Resposta(Base):
    __tablename__ = "respostas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    texto = Column(String, nullable=False)
    questao_id = Column(Integer, ForeignKey("questoes.id"), nullable=False)
    correta = Column(Boolean, default=False, nullable=False) 

    questao = relationship("Questao", back_populates="respostas")
