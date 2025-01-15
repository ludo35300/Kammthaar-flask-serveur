from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint
from dto.batteryStatus_schema import BatteryStatusSchema
from services import batteryStatus_service

blp_domaine_externe = Blueprint("batterieStatus_controller", "Status de la batterie", url_prefix="/battery", description="Récupération des données de la batterie")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200"))

@blp_domaine_externe.route('/realtime')
class BatterieRealtime(MethodView):
    @blp_domaine_externe.response(200, BatteryStatusSchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie en temps réel 
        -> Si système en ligne
        """
        return  batteryStatus_service.get_realtime()

@blp_domaine_externe.route('/last')
class BatterieLastRecord(MethodView):
    @blp_domaine_externe.response(200, BatteryStatusSchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return batteryStatus_service.get_last()