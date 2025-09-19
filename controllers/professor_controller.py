from flask import request, jsonify
from models.professor import Professor, db

class ProfessorController:

    @staticmethod
    def get_professores():
        professores = Professor.query.all()
        return jsonify([prof.to_dict() for prof in professores]), 200

    @staticmethod
    def get_professor_by_id(professor_id):
        professor = Professor.query.get(professor_id)
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404
        return jsonify(professor.to_dict()), 200

    @staticmethod
    def create_professor():
        data = request.get_json()
        if not data or "nome" not in data or "email" not in data:
            return jsonify({"error": "Dados inválidos"}), 400

        novo_professor = Professor(
            nome=data["nome"],
            email=data["email"],
            departamento=data.get("departamento")
        )
        db.session.add(novo_professor)
        db.session.commit()

        return jsonify(novo_professor.to_dict()), 201

    @staticmethod
    def update_professor(professor_id):
        professor = Professor.query.get(professor_id)
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404

        data = request.get_json()
        professor.nome = data.get("nome", professor.nome)
        professor.email = data.get("email", professor.email)
        professor.departamento = data.get("departamento", professor.departamento)

        db.session.commit()
        return jsonify(professor.to_dict()), 200

    @staticmethod
    def delete_professor(professor_id):
        professor = Professor.query.get(professor_id)
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404

        db.session.delete(professor)
        db.session.commit()
        return jsonify({"message": "Professor deletado com sucesso"}), 200
