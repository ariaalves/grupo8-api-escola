from flask import request, jsonify
from models.notas import Nota, db

class NotaController:

    @staticmethod
    def _get_data():
        data = request.get_json()
        if not data:
            return None, jsonify({"error": "Dados inválidos"}), 400
        return data, None, None

    @staticmethod
    def get_notas():
        notas = Nota.query.all()
        return jsonify([n.to_dict() for n in notas]), 200

    @staticmethod
    def get_nota_by_id(nota_id):
        nota = Nota.query.get(nota_id)
        if not nota:
            return jsonify({"error": "Nota não encontrada"}), 404
        return jsonify(nota.to_dict()), 200

    @staticmethod
    def create_nota():
        data, error_response, status = NotaController._get_data()
        if error_response:
            return error_response, status

        obrigatorios = ["nota", "aluno_id", "atividade_id"]
        for campo in obrigatorios:
            if campo not in data:
                return jsonify({"error": f"Campo obrigatório '{campo}' ausente"}), 400

        try:
            nova_nota = Nota(
                nota=data["nota"],
                aluno_id=data["aluno_id"],
                atividade_id=data["atividade_id"]
            )
            db.session.add(nova_nota)
            db.session.commit()
            return jsonify(nova_nota.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Erro ao criar nota: {str(e)}"}), 500

    @staticmethod
    def update_nota(nota_id):
        nota = Nota.query.get(nota_id)
        if not nota:
            return jsonify({"error": "Nota não encontrada"}), 404

        data, error_response, status = NotaController._get_data()
        if error_response:
            return error_response, status

        try:
            if "nota" in data:
                nota.nota = data["nota"]
            if "aluno_id" in data:
                nota.aluno_id = data["aluno_id"]
            if "atividade_id" in data:
                nota.atividade_id = data["atividade_id"]

            db.session.commit()
            return jsonify(nota.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Erro ao atualizar nota: {str(e)}"}), 500

    @staticmethod
    def delete_nota(nota_id):
        nota = Nota.query.get(nota_id)
        if not nota:
            return jsonify({"error": "Nota não encontrada"}), 404

        try:
            db.session.delete(nota)
            db.session.commit()
            return jsonify({"message": "Nota deletada com sucesso"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Erro ao deletar nota: {str(e)}"}), 500
