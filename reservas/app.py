from flask import Flask
from flasgger import Swagger
from models import db
from config import Config
from controllers.reservas_controller import ReservaController

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
swagger = Swagger(app)

@app.route("/reservas", methods=["GET"])
def get_reservas():
    """Listar todas as reservas
    ---
    tags: [Reservas]
    responses:
      200:
        description: Lista de reservas
    """
    return ReservaController.get_reservas()


@app.route("/reservas/<int:reserva_id>", methods=["GET"])
def get_reserva_by_id(reserva_id):
    """Buscar reserva por ID
    ---
    tags: [Reservas]
    parameters:
      - name: reserva_id
        in: path
        type: integer
        required: true
    responses:
      200: {description: Reserva encontrada}
      404: {description: Reserva não encontrada}
    """
    return ReservaController.get_reserva_by_id(reserva_id)


@app.route("/reservas", methods=["POST"])
def create_reserva():
    """Criar nova reserva
    ---
    tags: [Reservas]
    consumes: [application/json]
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            num_sala: {type: integer}
            lab: {type: boolean}
            data: {type: string, format: date}
            turma_id: {type: integer}
            hora_inicio: {type: string, example: "08:00"}
            hora_fim: {type: string, example: "10:00"}
    responses:
      201: {description: Reserva criada com sucesso}
      400: {description: Dados inválidos}
    """
    return ReservaController.create_reserva()


@app.route("/reservas/<int:reserva_id>", methods=["PUT"])
def update_reserva(reserva_id):
    """Atualizar uma reserva existente
    ---
    tags: [Reservas]
    parameters:
      - name: reserva_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            num_sala: {type: integer}
            lab: {type: boolean}
            data: {type: string, format: date}
            turma_id: {type: integer}
            hora_inicio: {type: string, example: "09:00"}
            hora_fim: {type: string, example: "11:00"}
    responses:
      200: {description: Reserva atualizada}
      404: {description: Reserva não encontrada}
    """
    return ReservaController.update_reserva(reserva_id)


@app.route("/reservas/<int:reserva_id>", methods=["DELETE"])
def delete_reserva(reserva_id):
    """Excluir uma reserva
    ---
    tags: [Reservas]
    parameters:
      - name: reserva_id
        in: path
        type: integer
        required: true
    responses:
      200: {description: Reserva deletada com sucesso}
      404: {description: Reserva não encontrada}
    """
    return ReservaController.delete_reserva(reserva_id)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
