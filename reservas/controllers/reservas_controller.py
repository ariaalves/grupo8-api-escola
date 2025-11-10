from flask import request, jsonify
from models.reservas import Reserva, db
from datetime import datetime

class ReservaController:

    @staticmethod
    def _get_json():
        data = request.get_json()
        if not data:
            return None, jsonify({"error": "Dados inválidos"}), 400
        return data, None, None

    @staticmethod
    def get_reservas():
        if request.method != 'GET':
            return jsonify({"error": "Método não permitido"}), 405

        reservas = Reserva.query.all()
        return jsonify([reserva.to_dict() for reserva in reservas]), 200

    @staticmethod
    def get_reserva_by_id(reserva_id):
        if request.method != 'GET':
            return jsonify({"error": "Método não permitido"}), 405

        reserva = Reserva.query.get(reserva_id)
        if not reserva:
            return jsonify({"error": "Reserva não encontrada"}), 404
        return jsonify(reserva.to_dict()), 200

    @staticmethod
    def create_reserva():
        if request.method != 'POST':
            return jsonify({"error": "Método não permitido"}), 405

        data, error_response, status = ReservaController._get_json()
        if error_response:
            return error_response, status

        if "num_sala" not in data or "lab" not in data or "data" not in data or "turma_id" not in data:
            return jsonify({"error": "Campos obrigatórios ausentes"}), 400

        try:
            data_reserva = datetime.fromisoformat(data["data"]).date()
        except ValueError:
            return jsonify({"error": "Data inválida, use o formato YYYY-MM-DD"}), 400

        nova_reserva = Reserva(
            num_sala=data["num_sala"],
            lab=bool(data["lab"]),
            data=data_reserva,
            turma_id=data["turma_id"]
        )

        db.session.add(nova_reserva)
        db.session.commit()
        return jsonify(nova_reserva.to_dict()), 201

    @staticmethod
    def update_reserva(reserva_id):
        if request.method != 'PUT':
         return jsonify({"error": "Método não permitido"}), 405

        reserva = Reserva.query.get(reserva_id)
        if not reserva:
         return jsonify({"error": "Reserva não encontrada"}), 404

        data, error_response, status = ReservaController._get_json()
        if error_response:
         return error_response, status

        campos = ["data", "turma_id", "num_sala", "lab"]

        for campo in campos:
            if campo in data:
            
                if campo == "data" and data[campo]:
                    try:
                     setattr(reserva, campo, datetime.strptime(data[campo], "%Y-%m-%d").date())
                    except ValueError:
                        return jsonify({"error": "Formato de data inválido. Use AAAA-MM-DD."}), 400
                else:
                    setattr(reserva, campo, data[campo])

        db.session.commit()
        return jsonify(reserva.to_dict()), 200


    @staticmethod
    def delete_reserva(reserva_id):
        if request.method != 'DELETE':
            return jsonify({"error": "Método não permitido"}), 405

        reserva = Reserva.query.get(reserva_id)
        if not reserva:
            return jsonify({"error": "Reserva não encontrada"}), 404

        db.session.delete(reserva)
        db.session.commit()
        return jsonify({"message": "Reserva deletada com sucesso"}), 200
