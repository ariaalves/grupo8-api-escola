from . import db

class Nota(db.Model):
    __tablename__ = 'notas'

    id = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Float)
    # aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    # atividade_id = db.Column(db.Integer, db.ForeignKey('atividades.id'), nullable=False)
    aluno_id = db.Column(db.Integer, nullable=False)
    atividade_id = db.Column(db.Integer, nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "nota": self.nota,
            "aluno_id": self.aluno_id,
            "atividade_id": self.atividade_id
        }
