from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint
from dto.discharging_status_schema import BaseDischargingStatusSchema
from services import discharging_status_service

blp_domaine_externe = Blueprint('discharging_controller', "Status de déchargement", url_prefix='/discharging', description="Récupération des données de déchargement")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200", "https://app.kammthaar.fr"))



@blp_domaine_externe.route('/realtime')
class DischargingRealtime(MethodView):
    @blp_domaine_externe.response(200, BaseDischargingStatusSchema())
    def get(self):
        """ 
        Récupère les données de déchargement de la batterie en temps réel 
        -> Si système en ligne
        """
        return  discharging_status_service.get_realtime()
    
@blp_domaine_externe.route('/last')
class DischargingLastRecord(MethodView):
    @blp_domaine_externe.response(200, BaseDischargingStatusSchema())
    def get(self):
        """ 
        Récupère les dernières données de déchargement de la batterie enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return discharging_status_service.get_last()
    