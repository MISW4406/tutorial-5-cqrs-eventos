import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import saludtech.servicio_ingestion.modulos.partnership.aplicacion
    import saludtech.servicio_ingestion.modulos.ingestion.aplicacion

def importar_modelos_alchemy():
    import saludtech.servicio_ingestion.modulos.partnership.infraestructura.dto 
    import saludtech.servicio_ingestion.modulos.ingestion.infraestructura.dto

def comenzar_consumidor():
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener 
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """

    import threading
    import saludtech.servicio_ingestion.modulos.partnership.infraestructura.consumidores as partnership
    import saludtech.servicio_ingestion.modulos.ingestion.infraestructura.consumidores as ingestion

    # Suscripción a eventos
    #threading.Thread(target=partnership.suscribirse_a_eventos).start()
    #threading.Thread(target=ingestion.suscribirse_a_eventos).start()

    # Suscripción a comandos
    #threading.Thread(target=partnership.suscribirse_a_comandos).start()
    #threading.Thread(target=ingestion.suscribirse_a_comandos).start()

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/ingestion"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = 'abc'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')
    

     # Inicializa la DB
    from saludtech.servicio_ingestion.config.db import init_db
    init_db(app)
    
    from saludtech.servicio_ingestion.config.db import db
    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor()

     # Importa Blueprints
    from . import partnership
    from . import ingestion

    # Registro de Blueprints
    app.register_blueprint(partnership.bp)
    app.register_blueprint(ingestion.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
