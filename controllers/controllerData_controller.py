from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint

from dto.controllerData_schema import ControllerDataSchema
from services import controllerData_service

blp_domaine_externe = Blueprint("controllerData_controller", "Données du controller", url_prefix="/controller", description="Récupération des données du controller")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200"))

@blp_domaine_externe.route('/realtime')
class BatterieRealtime(MethodView):
    @blp_domaine_externe.response(200, ControllerDataSchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie en temps réel 
        -> Si système en ligne
        """
        return  controllerData_service.get_realtime()

@blp_domaine_externe.route('/last')
class BatterieLastRecord(MethodView):
    @blp_domaine_externe.response(200, ControllerDataSchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return controllerData_service.get_last()