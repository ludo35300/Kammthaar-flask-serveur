from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint

from dto.energyStatistics_schema import EnergyStatisticsSchema
from services import energyStatistics_service


blp_domaine_externe = Blueprint("energyStatistics_controller", "Statistiques énergétiques", url_prefix="/statistics/energy", description="Récupération des statistiques énergétiques")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200"))

@blp_domaine_externe.route('/realtime')
class BatterieRealtime(MethodView):
    @blp_domaine_externe.response(200, EnergyStatisticsSchema())
    def get(self):
        """ 
        Récupère les dernières statistiques énergétiques en temps réel 
        -> Si système en ligne
        """
        return  energyStatistics_service.get_realtime()

@blp_domaine_externe.route('/last')
class BatterieLastRecord(MethodView):
    @blp_domaine_externe.response(200, EnergyStatisticsSchema())
    def get(self):
        """ 
        Récupère les dernières statistiques énergétiques enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return energyStatistics_service.get_last()
    
@blp_domaine_externe.route('/7days')
class BatterieLastRecord(MethodView):
    @blp_domaine_externe.response(200) # TODO: schema a faire
    def get(self):
        """ 
        Récupère les dernières statistiques énergétiques enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return energyStatistics_service.get_7days_data()