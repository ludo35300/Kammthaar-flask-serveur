from threading import Lock
from flask import Flask, request
from flask_cors import CORS
from flask_smorest import Api

from controllers.controller_controller import controller_controller
from controllers.statistiques_controller import statistiques_controller
from controllers.ps_controller import ps_controller
from controllers.battery_controller import batterie_controller
from controllers.battery_parametres_controller import batterie_parametres_controller
from controllers.server_controller import server_controller

# Création du verrou global pour bloquer les accès multiples au controller MPPT
mppt_lock = Lock()

def create_app():
    app = Flask(__name__)
    # Forcer l'utilisation de HTTPS
    # Talisman(app, force_https=True)
    app.debug = True
    
    # Configuration CORS
    #CORS(app, resources={r"/api/*": {"origins": ["*", "http://localhost:4200"]}})
    CORS(app, origins=["*"])
    
    # Initialisation de l'API
    app.config["API_TITLE"] = "Serveur du Kammthaar hors ligne"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/api/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)
    
    # Middleware pour attacher le verrou à chaque requête
    @app.before_request
    def attach_lock():
        request.environ['mppt_lock'] = mppt_lock

    # Enregistrement des blueprints
    api.register_blueprint(statistiques_controller)
    api.register_blueprint(controller_controller)
    api.register_blueprint(ps_controller)
    api.register_blueprint(batterie_controller)
    api.register_blueprint(batterie_parametres_controller)
    api.register_blueprint(server_controller)

    return app

# Création de l'application
app = create_app()

if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5000, ssl_context=('/ssl/kammthaar.fr_ssl_certificate.pem', '/ssl/private.pem'))
    app.run(host="0.0.0.0", port=5000)