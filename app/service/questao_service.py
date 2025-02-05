from sqlalchemy.orm import joinedload
from models.Questao import Questao
from sqlalchemy.sql import func


class QuestaoService:
    def __init__(self, db):
        self.db = db

    def obter_questoes_aleatorias(self, quantidade=10):
        return (self.db.query(Questao)
                    .options(joinedload(Questao.respostas))
                    .order_by(func.random())
                    .limit(quantidade)
                    .all())
        
    def obter_questao_por_id(self, questao_id):
        # Obtendo uma questão específica com suas respostas
        return self.db.query(Questao).options(joinedload(Questao.respostas)).filter(Questao.id == questao_id).first()

