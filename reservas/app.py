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
    return ReservaController.get_reservas()


@app.route("/reservas/<int:reserva_id>", methods=["GET"])
def get_reserva_by_id(reserva_id):
    return ReservaController.get_reserva_by_id(reserva_id)


@app.route("/reservas", methods=["POST"])
def create_reserva():
    return ReservaController.create_reserva()


@app.route("/reservas/<int:reserva_id>", methods=["PUT"])
def update_reserva(reserva_id):
    return ReservaController.update_reserva(reserva_id)


@app.route("/reservas/<int:reserva_id>", methods=["DELETE"])
def delete_reserva(reserva_id):
    return ReservaController.delete_reserva(reserva_id)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
