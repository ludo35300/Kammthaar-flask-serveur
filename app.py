from threading import Lock
from flask import Flask
from flask_cors import CORS
from flask_smorest import Api

from controllers import battery_controller, battery_parametres_controller, controller_controller, server_controller, ps_controller, statistiques_controller

# Création du verrou global pour bloquer les accès multiples au controller MPPT
mppt_lock = Lock()

def create_app():
    app = Flask(__name__)
    # Forcer l'utilisation de HTTPS
    # Talisman(app, force_https=True)
    app.debug = True
    
    # Configuration CORS
    #CORS(app, resources={r"/api/*": {"origins": ["*", "http://localhost:4200"]}})
    CORS(app, origins=["http://localhost:4200", "https://localhost:4200"])
    
    # Initialisation de l'API
    app.config["API_TITLE"] = "Kammthaar Data Hub"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.1.1"
    app.config["OPENAPI_URL_PREFIX"] = "/api/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
    

    api = Api(app)

    # Enregistrement des blueprints
    api.register_blueprint(statistiques_controller.blp_domaine_externe)
    api.register_blueprint(controller_controller.blp_domaine_externe)
    api.register_blueprint(ps_controller.blp_domaine_externe)
    api.register_blueprint(battery_controller.blp_domaine_externe)
    api.register_blueprint(battery_parametres_controller.blp_domaine_externe)
    api.register_blueprint(server_controller.blp_domaine_externe)

    return app

# Création de l'application
app = create_app()

if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5000, ssl_context=('/ssl/kammthaar.fr_ssl_certificate.pem', '/ssl/private.pem'))
    app.run(host="0.0.0.0", port=5000)