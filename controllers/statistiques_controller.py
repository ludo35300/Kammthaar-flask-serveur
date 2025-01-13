from flask import jsonify
from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint

from dto.statistiques_schema import BaseStatistiquesSchema
from services import statistiques_service

blp_domaine_externe = Blueprint('statistiques_controller', "Statistiques", url_prefix='/statistiques', description="Récupération des statistiques du controller MPPT")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200"))


@blp_domaine_externe.route('/realtime')
class ControllerRealtime(MethodView):
    @blp_domaine_externe.response(200, BaseStatistiquesSchema())
    def get(self):
        """ 
        Récupère les données du panneau solaire en temps réel 
        -> Si système en ligne
        """
        return  statistiques_service.get_realtime()
    
@blp_domaine_externe.route('/last')
class ControllerLastRecord(MethodView):
    @blp_domaine_externe.response(200, BaseStatistiquesSchema())
    def get(self):
        """ 
        Récupère les dernières données du panneau solaire enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return statistiques_service.get_last()
