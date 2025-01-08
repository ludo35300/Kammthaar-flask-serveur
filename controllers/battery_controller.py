from flask import jsonify
from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint
from dto.battery_schema import BaseBatterySchema
from models.battery_model import BatteryData
from services import batterie_service
from services import batterie_status_service

blp_domaine_externe = Blueprint('batterie_controller', "Batterie", url_prefix='/batterie', description="Récupération des données de la batterie")
CORS(blp_domaine_externe, origins="*") 

@blp_domaine_externe.route('/realtime')
class BatterieRealtime(MethodView):
    @blp_domaine_externe.response(200, BaseBatterySchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie en temps réel 
        -> Si système en ligne
        """
        return  batterie_service.get_batterie_data_realtime()
    
@blp_domaine_externe.route('/last')
class BatterieRealtime(MethodView):
    @blp_domaine_externe.response(200, BaseBatterySchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        # print(jsonify(batterie_service.get_last_data))
        return batterie_service.get_last_data()

@blp_domaine_externe.route('/last24h')
class Projets(MethodView):
    @blp_domaine_externe.response(200, BaseBatterySchema(many=True))
    def get(self):
        """
        Récupère la liste de données de la batterie des dernières 24 heures
        """
        return batterie_service.get_last_24h()




# @blp_domaine_externe.route('/last_status_data', methods=['GET'])
# def get_last_battery_status_data():
#     return batterie_status_service.get_last_batterie_status_data()




# @blp_domaine_externe.route('/status_realtime', methods=['GET'])
# def get_battery_status_data_realtime():
#     return batterie_status_service.get_batterie_status_data_realtime()

# @blp_domaine_externe.route('/last24hPourcent', methods=['GET'])
# def last_24h_pourcent():
#     return batterie_service.get_last_24h_pourcent()
    
# @blp_domaine_externe.route('/last24hAmperage', methods=['GET'])
# def last_24h_amperage():
#     return batterie_service.get_last_24h_amperage()
    
# @blp_domaine_externe.route('/last24hVoltage', methods=['GET'])
# def last_24h_voltage():
#     return batterie_service.get_last_24h_voltage()

# @blp_domaine_externe.route('/last24hPower', methods=['GET'])
# def last_24h_power():
#     return batterie_service.get_last_24h_power()
    
# @blp_domaine_externe.route('/last24hTemp', methods=['GET'])
# def last_24h_temp():
#     return batterie_service.get_last_24h_temp()