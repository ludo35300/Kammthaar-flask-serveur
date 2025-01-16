from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint
from dto.charging_status_schema import BaseChargingStatusSchema
from services import charging_status_service

blp_domaine_externe = Blueprint('charging_controller', "Status de chargement", url_prefix='/charging', description="Récupération des données de chargement")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200", "https://app.kammthaar.fr"))



@blp_domaine_externe.route('/realtime')
class ChargingRealtime(MethodView):
    @blp_domaine_externe.response(200, BaseChargingStatusSchema())
    def get(self):
        """ 
        Récupère les données du controller en temps réel 
        -> Si système en ligne
        """
        return  charging_status_service.get_realtime()
    
@blp_domaine_externe.route('/last')
class ChargingLastRecord(MethodView):
    @blp_domaine_externe.response(200, BaseChargingStatusSchema())
    def get(self):
        """ 
        Récupère les dernières données du controller enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return charging_status_service.get_last()
    