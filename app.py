from datetime import timedelta
import logging
import ssl
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_smorest import Api


from constantes.constantes import Config
from controllers import authentification_controller, batteryParameters_controller, batteryParameters_controller, batteryStatus_controller, breadcrumb_controller, chargingEquipmentStatus_controller, controllerData_controller, dailyStatistics_controller, dischargingEquipmentStatus_controller, energyStatistics_controller, loadData_controller, server_controller, solarData_controller


def create_app():
    app = Flask(__name__)
    # Forcer l'utilisation de HTTPS
    # Talisman(app, force_https=True)
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    
    
    # Initialisation de l'API
    app.config["API_TITLE"] = "Kammthaar Data Hub"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.1.1"
    app.config["OPENAPI_URL_PREFIX"] = "/api/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
    # Configuration JWT
    app.config["JWT_SECRET_KEY"] = Config.TOKEN
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=60)  # Durée d'expiration de l'access_token
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)   # Durée d'expiration du refresh_token
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config["JWT_COOKIE_SECURE"] = True  # À mettre sur True en production (HTTPS requis)
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False  # Désactiver la protection CSRF (à activer si nécessaire)
    app.config['JWT_CSRF_IN_COOKIES'] = True
    app.config['JWT_COOKIE_SAMESITE'] = 'None'
    jwt = JWTManager(app)
    
    # Configuration CORS
    CORS(app, origins=["http://localhost:4200", "https://localhost:4200", "https://app.kammthaar.fr"], supports_credentials=True)

    api = Api(app)

    # Enregistrement des blueprints
    api.register_blueprint(breadcrumb_controller.blp_domaine_externe)
    api.register_blueprint(batteryParameters_controller.blp_domaine_externe)
    api.register_blueprint(batteryStatus_controller.blp_domaine_externe)
    api.register_blueprint(chargingEquipmentStatus_controller.blp_domaine_externe)
    api.register_blueprint(controllerData_controller.blp_domaine_externe)
    api.register_blueprint(dailyStatistics_controller.blp_domaine_externe)
    api.register_blueprint(dischargingEquipmentStatus_controller.blp_domaine_externe)
    api.register_blueprint(energyStatistics_controller.blp_domaine_externe)
    api.register_blueprint(loadData_controller.blp_domaine_externe)
    api.register_blueprint(solarData_controller.blp_domaine_externe)
    api.register_blueprint(authentification_controller.blp_domaine_externe)
    api.register_blueprint(server_controller.blp_domaine_externe)

    return app

# Création de l'application
app = create_app()


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5000, ssl_context=('/ssl/kammthaar.fr_ssl_certificate.pem', '/ssl/private.pem'))
    app.run(host="0.0.0.0", port=5000)