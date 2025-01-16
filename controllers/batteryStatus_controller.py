from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint
from dto.batteryStatus_schema import BatteryStatusSchema, Value24hSchema
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
    
@blp_domaine_externe.route('/last/24h/<string:data_type>')
class Last24hData(MethodView):
    @blp_domaine_externe.response(200, Value24hSchema(many=True))
    def get(self, data_type):
        """ 
            Récupère toutes les valeurs d'une donnée spécifique enregistrées dans InfluxDB sur les dernières 24 heures ainsi que la date/heure de l'enregistrement.
        """
        valid_columns = ["voltage", "current", "power", "temperature", "state_of_charge"]
        if data_type not in valid_columns:
            return {"erreur": f"'{data_type}' n'est pas un type de donnée valide."}, 400
        return batteryStatus_service.get_last_24h_data(data_type)