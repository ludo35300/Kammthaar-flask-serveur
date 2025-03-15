from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint

from dto.batteryParameters_schema import BatteryParametersSchema
from services import batteryParameters_service

blp_domaine_externe = Blueprint("batteryParameters_controller", "Paramètres de la batterie", url_prefix="/battery/parameters", description="Récupération des paramètres de la batterie")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200"))

@blp_domaine_externe.route('/realtime')
class BatterieRealtime(MethodView):
    @blp_domaine_externe.response(200, BatteryParametersSchema())
    def get(self):
        """ 
        Récupère les derniers paramètres de la batterie en temps réel 
        -> Si système en ligne
        """
        return  batteryParameters_service.get_realtime()

@blp_domaine_externe.route('/last')
class BatterieLastRecord(MethodView):
    @blp_domaine_externe.response(200, BatteryParametersSchema())
    def get(self):
        """ 
        Récupère les derniers paramètres de la batterie enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return batteryParameters_service.get_last()