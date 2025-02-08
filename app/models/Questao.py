from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database.database import Base
from enums.NivelDificuldade import NivelDificuldade


class Questao(Base):
    __tablename__ = "questoes"

    id = Column(Integer, primary_key=True)
    pergunta = Column(String, nullable=False)
    nivel = Column(Enum(NivelDificuldade), nullable=False)

    respostas = relationship("Resposta", back_populates="questao", cascade="all, delete-orphan", lazy="select")
