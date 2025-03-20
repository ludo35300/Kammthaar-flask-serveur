from flask.views import MethodView
from flask_cors import CORS
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from dto.controllerData_schema import ControllerDataSchema
from services import controllerData_service

blp_domaine_externe = Blueprint("controllerData_controller", "Données du controller", url_prefix="/controller", description="Récupération des données du controller")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200", "https://app.kammthaar.fr"), supports_credentials=True)

@blp_domaine_externe.route('/realtime')
class ControllerRealtime(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, ControllerDataSchema())
    def get(self):
        """ 
        Récupère les dernières données du controller en temps réel 
        -> Si système en ligne
        """
        return  controllerData_service.get_realtime()

@blp_domaine_externe.route('/last')
class ControllerLastRecord(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, ControllerDataSchema())
    def get(self):
        """ 
        Récupère les dernières données du controller enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return controllerData_service.get_last()