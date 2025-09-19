from flask import request, jsonify
from models.turma import Turma, db

class TurmaController:

    @staticmethod
    def get_turmas():
        turmas = Turma.query.all()
        return jsonify([turma.to_dict() for turma in turmas]), 200

    @staticmethod
    def get_turma_by_id(turma_id):
        turma = Turma.query.get(turma_id)
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404
        return jsonify(turma.to_dict()), 200

    @staticmethod
    def create_turma():
        data = request.get_json()
        if not data or "nome" not in data or "ano" not in data:
            return jsonify({"error": "Dados inválidos"}), 400

        nova_turma = Turma(
            nome=data["nome"],
            ano=data["ano"],
            turno=data.get("turno")
        )
        db.session.add(nova_turma)
        db.session.commit()

        return jsonify(nova_turma.to_dict()), 201

    @staticmethod
    def update_turma(turma_id):
        turma = Turma.query.get(turma_id)
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404

        data = request.get_json()
        turma.nome = data.get("nome", turma.nome)
        turma.ano = data.get("ano", turma.ano)
        turma.turno = data.get("turno", turma.turno)

        db.session.commit()
        return jsonify(turma.to_dict()), 200

    @staticmethod
    def delete_turma(turma_id):
        turma = Turma.query.get(turma_id)
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404

        db.session.delete(turma)
        db.session.commit()
        return jsonify({"message": "Turma deletada com sucesso"}), 200
