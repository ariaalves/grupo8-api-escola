from flask import Flask
from models import db
from config import Config
from controllers.aluno_controller import AlunoController
from controllers.turma_controller import TurmaController
from controllers.professor_controller import ProfessorController

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/alunos", methods=["GET"])
def get_alunos():
    return AlunoController.get_alunos()

@app.route("/alunos/<int:aluno_id>", methods=["GET"])
def get_aluno_by_id(aluno_id):
    return AlunoController.get_aluno_by_id(aluno_id)

@app.route("/alunos", methods=["POST"])
def create_aluno():
    return AlunoController.create_aluno()

@app.route("/alunos/<int:aluno_id>", methods=["PUT"])
def update_aluno(aluno_id):
    return AlunoController.update_aluno(aluno_id)

@app.route("/alunos/<int:aluno_id>", methods=["DELETE"])
def delete_aluno(aluno_id):
    return AlunoController.delete_aluno(aluno_id)

@app.route("/turmas", methods=["GET"])
def get_turmas():
    return TurmaController.get_turmas()

@app.route("/turmas/<int:turma_id>", methods=["GET"])
def get_turma_by_id(turma_id):
    return TurmaController.get_turma_by_id(turma_id)

@app.route("/turmas", methods=["POST"])
def create_turma():
    return TurmaController.create_turma()

@app.route("/turmas/<int:turma_id>", methods=["PUT"])
def update_turma(turma_id):
    return TurmaController.update_turma(turma_id)

@app.route("/turmas/<int:turma_id>", methods=["DELETE"])
def delete_turma(turma_id):
    return TurmaController.delete_turma(turma_id)

@app.route("/professores", methods=["GET"])
def get_professores():
    return ProfessorController.get_professores()

@app.route("/professores/<int:professor_id>", methods=["GET"])
def get_professor_by_id(professor_id):
    return ProfessorController.get_professor_by_id(professor_id)

@app.route("/professores", methods=["POST"])
def create_professor():
    return ProfessorController.create_professor()

@app.route("/professores/<int:professor_id>", methods=["PUT"])
def update_professor(professor_id):
    return ProfessorController.update_professor(professor_id)

@app.route("/professores/<int:professor_id>", methods=["DELETE"])
def delete_professor(professor_id):
    return ProfessorController.delete_professor(professor_id)

def init_db():
    with app.app_context():
        db.create_all()
        print("Banco de dados inicializado!")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
