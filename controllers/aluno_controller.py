from flask import request, jsonify
from models.aluno import Aluno, db

class AlunoController:

    @staticmethod
    def get_alunos():
        alunos = Aluno.query.all()
        return jsonify([aluno.to_dict() for aluno in alunos]), 200

    @staticmethod
    def get_aluno_by_id(aluno_id):
        aluno = Aluno.query.get(aluno_id)
        if not aluno:
            return jsonify({"error": "Aluno não encontrado"}), 404
        return jsonify(aluno.to_dict()), 200

    @staticmethod
    def create_aluno():
        data = request.get_json()
        if not data or "nome" not in data or "email" not in data:
            return jsonify({"error": "Dados inválidos"}), 400

        novo_aluno = Aluno(
            nome=data["nome"],
            email=data["email"],
            curso=data.get("curso")
        )
        db.session.add(novo_aluno)
        db.session.commit()

        return jsonify(novo_aluno.to_dict()), 201

    @staticmethod
    def update_aluno(aluno_id):
        aluno = Aluno.query.get(aluno_id)
        if not aluno:
            return jsonify({"error": "Aluno não encontrado"}), 404

        data = request.get_json()
        aluno.nome = data.get("nome", aluno.nome)
        aluno.email = data.get("email", aluno.email)
        aluno.curso = data.get("curso", aluno.curso)

        db.session.commit()
        return jsonify(aluno.to_dict()), 200

    @staticmethod
    def delete_aluno(aluno_id):
        aluno = Aluno.query.get(aluno_id)
        if not aluno:
            return jsonify({"error": "Aluno não encontrado"}), 404

        db.session.delete(aluno)
        db.session.commit()
        return jsonify({"message": "Aluno deletado com sucesso"}), 200
