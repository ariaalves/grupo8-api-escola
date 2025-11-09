from flask import request, jsonify
from datetime import datetime
from models.atividade import Atividade, db

class AtividadeController:

    @staticmethod
    def _get_data():
        data = request.get_json()
        if not data:
            return None, jsonify({"error": "Dados inválidos"}), 400
        return data, None, None

    @staticmethod
    def get_atividades():
        if request.method != 'GET':
            return jsonify({"error": "Método não permitido"}), 405

        atividades = Atividade.query.all()
        return jsonify([atividade.to_dict() for atividade in atividades]), 200

    @staticmethod
    def get_atividade_by_id(atividade_id):
        if request.method != 'GET':
            return jsonify({"error": "Método não permitido"}), 405

        atividade = Atividade.query.get(atividade_id)
        if not atividade:
            return jsonify({"error": "Atividade não encontrada"}), 404

        return jsonify(atividade.to_dict()), 200

    @staticmethod
    def create_atividade():
        if request.method != 'POST':
            return jsonify({"error": "Método não permitido"}), 405

        data, error_response, status = AtividadeController._get_data()
        if error_response:
            return error_response, status

        obrigatorios = ["nome_atividade", "peso_porcento", "data_entrega", "turma_id", "professor_id"]
        for campo in obrigatorios:
            if campo not in data:
                return jsonify({"error": f"Campo obrigatório '{campo}' ausente"}), 400

        try:
            nova_atividade = Atividade(
                nome_atividade=data["nome_atividade"],
                descricao=data.get("descricao"),
                peso_porcento=data["peso_porcento"],
                data_entrega=datetime.strptime(data["data_entrega"], "%Y-%m-%d").date(),
                turma_id=data["turma_id"],
                professor_id=data["professor_id"]
            )
            db.session.add(nova_atividade)
            db.session.commit()
            return jsonify(nova_atividade.to_dict()), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Erro ao criar atividade: {str(e)}"}), 500

    @staticmethod
    def update_atividade(atividade_id):
        if request.method != 'PUT':
            return jsonify({"error": "Método não permitido"}), 405

        atividade = Atividade.query.get(atividade_id)
        if not atividade:
            return jsonify({"error": "Atividade não encontrada"}), 404

        data, error_response, status = AtividadeController._get_data()
        if error_response:
            return error_response, status

        campos = ["nome_atividade", "descricao", "peso_porcento", "data_entrega", "turma_id", "professor_id"]
        for campo in campos:
            if campo in data:
                if campo == "data_entrega" and data[campo]:
                    setattr(atividade, campo, datetime.strptime(data[campo], "%Y-%m-%d").date())
                else:
                    setattr(atividade, campo, data[campo])

        try:
            db.session.commit()
            return jsonify(atividade.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Erro ao atualizar atividade: {str(e)}"}), 500

    @staticmethod
    def delete_atividade(atividade_id):
        if request.method != 'DELETE':
            return jsonify({"error": "Método não permitido"}), 405

        atividade = Atividade.query.get(atividade_id)
        if not atividade:
            return jsonify({"error": "Atividade não encontrada"}), 404

        try:
            db.session.delete(atividade)
            db.session.commit()
            return jsonify({"message": "Atividade deletada com sucesso"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Erro ao deletar atividade: {str(e)}"}), 500
