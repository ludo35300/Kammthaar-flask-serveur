from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint
from dto.battery_schema import BaseBatterySchema, Value24hSchema
from services import batterie_service
from services import batterie_status_service

blp_domaine_externe = Blueprint('batterie_controller', "Batterie", url_prefix='/batterie', description="Récupération des données de la batterie")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200"))

@blp_domaine_externe.route('/realtime')
class BatterieRealtime(MethodView):
    @blp_domaine_externe.response(200, BaseBatterySchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie en temps réel 
        -> Si système en ligne
        """
        return  batterie_service.get_batterie_data_realtime().json()
    
@blp_domaine_externe.route('/last')
class BatterieLastRecord(MethodView):
    @blp_domaine_externe.response(200, BaseBatterySchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return batterie_service.get_last_data()
    
@blp_domaine_externe.route('/last/24h/<string:data_type>')
@blp_domaine_externe.doc(params={'data_type': 'Type de données: "battery_voltage", "battery_amperage"'})
class Last24hData(MethodView):
    @blp_domaine_externe.response(200, Value24hSchema(many=True))
    def get(self, data_type):
        """ 
            Récupère toutes les valeurs d'une donnée spécifique enregistrées dans InfluxDB sur les dernières 24 heures ainsi que la date/heure de l'enregistrement.
        """
        valid_columns = ["battery_voltage", "battery_amperage", "battery_power", "battery_temp", "battery_pourcent"]
        if data_type not in valid_columns:
            return {"erreur": f"'{data_type}' n'est pas un type de donnée valide."}, 400
        return batterie_service.get_last_24h_data(data_type)