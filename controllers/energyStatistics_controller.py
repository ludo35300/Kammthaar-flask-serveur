from flask.views import MethodView
from flask_cors import CORS
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from dto.energyStatistics_schema import EnergyStatisticsSchema
from services import energyStatistics_service


blp_domaine_externe = Blueprint("energyStatistics_controller", "Statistiques énergétiques", url_prefix="/statistics/energy", description="Récupération des statistiques énergétiques")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200", "https://app.kammthaar.fr"), supports_credentials=True)

@blp_domaine_externe.route('/realtime')
class BatterieRealtime(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, EnergyStatisticsSchema())
    def get(self):
        """ 
        Récupère les dernières statistiques énergétiques en temps réel 
        -> Si système en ligne
        """
        return  energyStatistics_service.get_realtime()

@blp_domaine_externe.route('/last')
class BatterieLastRecord(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, EnergyStatisticsSchema())
    def get(self):
        """ 
        Récupère les dernières statistiques énergétiques enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return energyStatistics_service.get_last()