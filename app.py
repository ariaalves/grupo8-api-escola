from flask import Flask
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

def init_db():
    with app.app_context():
        db.create_all()
        print("Banco de dados inicializado!")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
