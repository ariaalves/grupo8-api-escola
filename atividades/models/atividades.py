from . import db

class Atividade(db.Model):
    __tablename__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    nome_atividade = db.Column(db.String(50),nullable=False)
    descricao = db.Column(db.String(100))
    peso_porcento = db.Column(db.Integer,nullable=False)
    data_entrega = db.Column(db.Date, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)