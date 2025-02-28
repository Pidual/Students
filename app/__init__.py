# Este archivo crea y configura la FLASK API

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

#Inicializar SQL alchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # inicializar la base de datos
    db.init_app(app)

    # Register blueprints (routes)
    from .routes import main
    app.register_blueprint(main)

    return app