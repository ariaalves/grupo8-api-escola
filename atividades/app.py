from flask import Flask
from flasgger import Swagger
from models import db
from models.atividades import Atividade
from models.notas import Nota
from config import Config
from controllers.atividades_controller import AtividadeController
from controllers.notas_controller import NotaController

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "API de Atividades e Notas",
        "description": "Microsserviço responsável pelo gerenciamento de atividades e notas.",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["http"]
})


@app.route("/atividades", methods=["GET"])
def get_atividades():
    """Listar todas as atividades
    ---
    tags: [Atividades]
    responses:
      200:
        description: Lista de atividades cadastradas
    """
    return AtividadeController.get_atividades()

@app.route("/atividades/<int:atividade_id>", methods=["GET"])
def get_atividade_by_id(atividade_id):
    """Buscar atividade por ID
    ---
    tags: [Atividades]
    parameters:
      - name: atividade_id
        in: path
        type: integer
        required: true
    responses:
      200: {description: Atividade encontrada}
      404: {description: Atividade não encontrada}
    """
    return AtividadeController.get_atividade_by_id(atividade_id)

@app.route("/atividades", methods=["POST"])
def create_atividade():
    """Criar nova atividade
    ---
    tags: [Atividades]
    consumes: [application/json]
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            nome_atividade: {type: string}
            descricao: {type: string}
            peso_porcento: {type: integer}
            data_entrega: {type: string, format: date}
            turma_id: {type: integer}
            professor_id: {type: integer}
    responses:
      201: {description: Atividade criada com sucesso}
      400: {description: Dados inválidos ou campos ausentes}
    """
    return AtividadeController.create_atividade()

@app.route("/atividades/<int:atividade_id>", methods=["PUT"])
def update_atividade(atividade_id):
    """Atualizar atividade existente
    ---
    tags: [Atividades]
    parameters:
      - name: atividade_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            nome_atividade: {type: string}
            descricao: {type: string}
            peso_porcento: {type: integer}
            data_entrega: {type: string, format: date}
            turma_id: {type: integer}
            professor_id: {type: integer}
    responses:
      200: {description: Atividade atualizada com sucesso}
      404: {description: Atividade não encontrada}
    """
    return AtividadeController.update_atividade(atividade_id)

@app.route("/atividades/<int:atividade_id>", methods=["DELETE"])
def delete_atividade(atividade_id):
    """Excluir atividade
    ---
    tags: [Atividades]
    parameters:
      - name: atividade_id
        in: path
        type: integer
        required: true
    responses:
      200: {description: Atividade deletada com sucesso}
      404: {description: Atividade não encontrada}
    """
    return AtividadeController.delete_atividade(atividade_id)

@app.route("/notas", methods=["GET"])
def get_notas():
    """Listar todas as notas
    ---
    tags: [Notas]
    responses:
      200:
        description: Lista de notas cadastradas
    """
    return NotaController.get_notas()

@app.route("/notas/<int:nota_id>", methods=["GET"])
def get_nota_by_id(nota_id):
    """Buscar nota por ID
    ---
    tags: [Notas]
    parameters:
      - name: nota_id
        in: path
        type: integer
        required: true
    responses:
      200: {description: Nota encontrada}
      404: {description: Nota não encontrada}
    """
    return NotaController.get_nota_by_id(nota_id)

@app.route("/notas", methods=["POST"])
def create_nota():
    """Criar nova nota
    ---
    tags: [Notas]
    consumes: [application/json]
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            nota: {type: number, format: float}
            aluno_id: {type: integer}
            atividade_id: {type: integer}
    responses:
      201: {description: Nota criada com sucesso}
      400: {description: Dados inválidos ou campos ausentes}
    """
    return NotaController.create_nota()

@app.route("/notas/<int:nota_id>", methods=["PUT"])
def update_nota(nota_id):
    """Atualizar nota existente
    ---
    tags: [Notas]
    parameters:
      - name: nota_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            nota: {type: number, format: float}
            aluno_id: {type: integer}
            atividade_id: {type: integer}
    responses:
      200: {description: Nota atualizada com sucesso}
      404: {description: Nota não encontrada}
    """
    return NotaController.update_nota(nota_id)

@app.route("/notas/<int:nota_id>", methods=["DELETE"])
def delete_nota(nota_id):
    """Excluir nota
    ---
    tags: [Notas]
    parameters:
      - name: nota_id
        in: path
        type: integer
        required: true
    responses:
      200: {description: Nota deletada com sucesso}
      404: {description: Nota não encontrada}
    """
    return NotaController.delete_nota(nota_id)

def init_db():
    with app.app_context():
        db.create_all()
        print("Banco de dados de Atividades inicializado!")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
