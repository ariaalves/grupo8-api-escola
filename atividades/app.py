from flask import Flask
from models import db
from config import Config
from controllers.atividades_controller import AtividadeController
from controllers.notas_controller import NotaController

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/atividades", methods=["GET"])
def get_atividades():
    return AtividadeController.get_atividades()

@app.route("/atividades/<int:atividade_id>", methods=["GET"])
def get_atividade_by_id(atividade_id):
    return AtividadeController.get_atividade_by_id(atividade_id)

@app.route("/atividades", methods=["POST"])
def create_atividade():
    return AtividadeController.create_atividade()

@app.route("/atividades/<int:atividade_id>", methods=["PUT"])
def update_atividade(atividade_id):
    return AtividadeController.update_atividade(atividade_id)

@app.route("/atividades/<int:atividade_id>", methods=["DELETE"])
def delete_atividade(atividade_id):
    return AtividadeController.delete_atividade(atividade_id)

@app.route("/notas", methods=["GET"])
def get_notas():
    return NotaController.get_notas()

@app.route("/notas/<int:nota_id>", methods=["GET"])
def get_nota_by_id(nota_id):
    return NotaController.get_nota_by_id(nota_id)

@app.route("/notas", methods=["POST"])
def create_nota():
    return NotaController.create_nota()

@app.route("/notas/<int:nota_id>", methods=["PUT"])
def update_nota(nota_id):
    return NotaController.update_nota(nota_id)

@app.route("/notas/<int:nota_id>", methods=["DELETE"])
def delete_nota(nota_id):
    return NotaController.delete_nota(nota_id)

def init_db():
    with app.app_context():
        db.create_all()
        print("Banco de dados de Atividades inicializado!")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5003, debug=True)


