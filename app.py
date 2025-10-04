from flask import Flask
from models import db
from config import Config
from controllers.aluno_controller import AlunoController
from controllers.turma_controller import TurmaController
from controllers.professor_controller import ProfessorController
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API Escola",
        "description": "API para gerenciamento de alunos, turmas e professores.",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["http"],
    "definitions": {
        "Aluno": {
            "type": "object",
            "properties": {
                "id": {"type": "integer", "example": 1},
                "nome": {"type": "string", "example": "João Silva"},
                "idade": {"type": "integer", "example": 16},
                "data_nascimento": {"type": "string", "format": "date", "example": "2008-05-10"},
                "turma_id": {"type": "integer", "example": 2},
                "nota_primeiro_semestre": {"type": "number", "example": 8.5},
                "nota_segundo_semestre": {"type": "number", "example": 7.0},
                "media_final": {"type": "number", "example": 7.25}
            },
            "required": ["nome", "idade", "data_nascimento", "turma_id"]
        },
        "Turma": {
            "type": "object",
            "properties": {
                "id": {"type": "integer", "example": 2},
                "descricao": {"type": "string", "example": "2º Ano A"},
                "professor_id": {"type": "integer", "example": 1},
                "ativo": {"type": "boolean", "example": True}
            },
            "required": ["descricao", "professor_id"]
        },
        "Professor": {
            "type": "object",
            "properties": {
                "id": {"type": "integer", "example": 3},
                "nome": {"type": "string", "example": "Maria Oliveira"},
                "idade": {"type": "integer", "example": 40},
                "materia": {"type": "string", "example": "Matemática"},
                "observacoes": {"type": "string", "example": "Disponível no período da manhã"}
            },
            "required": ["nome", "idade", "materia"]
        }
    }
}

swagger = Swagger(app, template=swagger_template)

@app.route("/alunos", methods=["GET"])
def get_alunos():
    """
    Lista todos os alunos
    ---
    tags:
      - Alunos
    responses:
      200:
        description: Lista de alunos
        schema:
          type: array
          items:
            $ref: '#/definitions/Aluno'
    """
    return AlunoController.get_alunos()

@app.route("/alunos/<int:aluno_id>", methods=["GET"])
def get_aluno_by_id(aluno_id):
    """
    Retorna um aluno por ID
    ---
    tags:
      - Alunos
    parameters:
      - name: aluno_id
        in: path
        type: integer
        required: true
        description: ID do aluno
    responses:
      200:
        description: Aluno encontrado
        schema:
          $ref: '#/definitions/Aluno'
      404:
        description: Aluno não encontrado
    """
    return AlunoController.get_aluno_by_id(aluno_id)

@app.route("/alunos", methods=["POST"])
def create_aluno():
    """
    Cria um novo aluno
    ---
    tags:
      - Alunos
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Aluno'
    responses:
      201:
        description: Aluno criado
        schema:
          $ref: '#/definitions/Aluno'
      400:
        description: Requisição inválida
    """
    return AlunoController.create_aluno()

@app.route("/alunos/<int:aluno_id>", methods=["PUT"])
def update_aluno(aluno_id):
    """
    Atualiza um aluno por ID
    ---
    tags:
      - Alunos
    consumes:
      - application/json
    parameters:
      - name: aluno_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Aluno'
    responses:
      200:
        description: Aluno atualizado
        schema:
          $ref: '#/definitions/Aluno'
      404:
        description: Aluno não encontrado
    """
    return AlunoController.update_aluno(aluno_id)

@app.route("/alunos/<int:aluno_id>", methods=["DELETE"])
def delete_aluno(aluno_id):
    """
    Remove um aluno por ID
    ---
    tags:
      - Alunos
    parameters:
      - name: aluno_id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Aluno deletado com sucesso
      404:
        description: Aluno não encontrado
    """
    return AlunoController.delete_aluno(aluno_id)

@app.route("/turmas", methods=["GET"])
def get_turmas():
    """
    Lista todas as turmas
    ---
    tags:
      - Turmas
    responses:
      200:
        description: Lista de turmas
        schema:
          type: array
          items:
            $ref: '#/definitions/Turma'
    """
    return TurmaController.get_turmas()

@app.route("/turmas/<int:turma_id>", methods=["GET"])
def get_turma_by_id(turma_id):
    """
    Retorna uma turma por ID
    ---
    tags:
      - Turmas
    parameters:
      - name: turma_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Turma encontrada
        schema:
          $ref: '#/definitions/Turma'
      404:
        description: Turma não encontrada
    """
    return TurmaController.get_turma_by_id(turma_id)

@app.route("/turmas", methods=["POST"])
def create_turma():
    """
    Cria uma nova turma
    ---
    tags:
      - Turmas
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Turma'
    responses:
      201:
        description: Turma criada
        schema:
          $ref: '#/definitions/Turma'
      400:
        description: Requisição inválida
    """
    return TurmaController.create_turma()

@app.route("/turmas/<int:turma_id>", methods=["PUT"])
def update_turma(turma_id):
    """
    Atualiza uma turma por ID
    ---
    tags:
      - Turmas
    consumes:
      - application/json
    parameters:
      - name: turma_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Turma'
    responses:
      200:
        description: Turma atualizada
        schema:
          $ref: '#/definitions/Turma'
      404:
        description: Turma não encontrada
    """
    return TurmaController.update_turma(turma_id)

@app.route("/turmas/<int:turma_id>", methods=["DELETE"])
def delete_turma(turma_id):
    """
    Remove uma turma por ID
    ---
    tags:
      - Turmas
    parameters:
      - name: turma_id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Turma deletada com sucesso
      404:
        description: Turma não encontrada
    """
    return TurmaController.delete_turma(turma_id)

@app.route("/professores", methods=["GET"])
def get_professores():
    """
    Lista todos os professores
    ---
    tags:
      - Professores
    responses:
      200:
        description: Lista de professores
        schema:
          type: array
          items:
            $ref: '#/definitions/Professor'
    """
    return ProfessorController.get_professores()

@app.route("/professores/<int:professor_id>", methods=["GET"])
def get_professor_by_id(professor_id):
    """
    Retorna um professor por ID
    ---
    tags:
      - Professores
    parameters:
      - name: professor_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Professor encontrado
        schema:
          $ref: '#/definitions/Professor'
      404:
        description: Professor não encontrado
    """
    return ProfessorController.get_professor_by_id(professor_id)

@app.route("/professores", methods=["POST"])
def create_professor():
    """
    Cria um novo professor
    ---
    tags:
      - Professores
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Professor'
    responses:
      201:
        description: Professor criado
        schema:
          $ref: '#/definitions/Professor'
      400:
        description: Requisição inválida
    """
    return ProfessorController.create_professor()

@app.route("/professores/<int:professor_id>", methods=["PUT"])
def update_professor(professor_id):
    """
    Atualiza um professor por ID
    ---
    tags:
      - Professores
    consumes:
      - application/json
    parameters:
      - name: professor_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Professor'
    responses:
      200:
        description: Professor atualizado
        schema:
          $ref: '#/definitions/Professor'
      404:
        description: Professor não encontrado
    """
    return ProfessorController.update_professor(professor_id)

@app.route("/professores/<int:professor_id>", methods=["DELETE"])
def delete_professor(professor_id):
    """
    Remove um professor por ID
    ---
    tags:
      - Professores
    parameters:
      - name: professor_id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Professor deletado com sucesso
      404:
        description: Professor não encontrado
    """
    return ProfessorController.delete_professor(professor_id)

def init_db():
    with app.app_context():
        db.create_all()
        print("Banco de dados inicializado!")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
