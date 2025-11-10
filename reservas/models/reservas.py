from . import db

class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    num_sala = db.Column(db.Integer, nullable=False)
    lab = db.Column(db.Boolean, default=False)
    data = db.Column(db.Date, nullable=False)
    # turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    turma_id = db.Column(db.Integer, nullable=False)



    def __init__(self, num_sala, lab, data, turma_id):
        self.num_sala = num_sala
        self.lab = lab
        self.data = data
        self.turma_id = turma_id

    def to_dict(self):
        return {
            "id": self.id,
            "num_sala": self.num_sala,
            "lab": self.lab,
            "data": self.data.isoformat() if self.data else None,
            "turma_id": self.turma_id
        }