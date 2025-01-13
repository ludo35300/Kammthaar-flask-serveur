from flask import jsonify
from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint

from dto.battery_parametres_schema import BaseBatteryParametresSchema
from services import batterie_parametres_service


blp_domaine_externe = Blueprint("batterie_parametres_controller", "Paramètres Batterie", url_prefix="/batterie/parametres", description="Récupération des paramètres de la batterie")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200"))

@blp_domaine_externe.route('/realtime')
class BatteriParametreseRealtime(MethodView):
    @blp_domaine_externe.response(200, BaseBatteryParametresSchema())
    def get(self):
        """ 
        Récupère les derniers paramètres de la batterie en temps réel 
        -> Si système en ligne
        """
        return  batterie_parametres_service.get_realtime()
    
@blp_domaine_externe.route('/last')
class BatterieParametreseLastRecord(MethodView):
    @blp_domaine_externe.response(200, BaseBatteryParametresSchema())
    def get(self):
        """ 
        Récupère les derniers paramètres de la batterie enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return batterie_parametres_service.get_last()
