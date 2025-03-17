from flask.views import MethodView
from flask_cors import CORS
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from dto.dailyStatistics_schema import DailyStatisticsSchema
from services import dailyStatistics_service

blp_domaine_externe = Blueprint("dailyStatistics_controller", "Statistiques journaliers", url_prefix="/statistics/daily", description="Récupération des statistiques journaliers")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200", "https://app.kammthaar.fr"), supports_credentials=True)

@blp_domaine_externe.route('/realtime')
class BatterieRealtime(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, DailyStatisticsSchema())
    def get(self):
        """ 
        Récupère les dernières statistiques journaliers en temps réel 
        -> Si système en ligne
        """
        return  dailyStatistics_service.get_realtime()

@blp_domaine_externe.route('/last')
class BatterieLastRecord(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, DailyStatisticsSchema())
    def get(self):
        """ 
        Récupère les dernières statistiques journaliers enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return dailyStatistics_service.get_last()