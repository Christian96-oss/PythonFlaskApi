from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)

# Menambahkan banyak asal yang diizinkan
CORS(app, origins=["http://localhost:5173", "http://localhost:5174", "http://localhost:3000"])  # Tambahkan asal lain jika perlu

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Inisialisasi JWTManager
jwt = JWTManager(app)

from app.model import user, dosen, mahasiswa, gambar
from app import routes

if __name__ == "__main__":
    app.run(debug=True)
