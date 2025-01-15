from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint

from dto.chargingEquipmentStatus_schema import ChargingEquipmentStatusSchema
from services import chargingEquipmentStatus_service

blp_domaine_externe = Blueprint("chargingEquipmentStatus_controller", "Status de la charge", url_prefix="/charging", description="Récupération des données du status del a charge")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200"))

@blp_domaine_externe.route('/realtime')
class ChargingEquipmentRealtime(MethodView):
    @blp_domaine_externe.response(200, ChargingEquipmentStatusSchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie en temps réel 
        -> Si système en ligne
        """
        return  chargingEquipmentStatus_service.get_realtime()

@blp_domaine_externe.route('/last')
class ChargingEquipmenLastRecord(MethodView):
    @blp_domaine_externe.response(200, ChargingEquipmentStatusSchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return chargingEquipmentStatus_service.get_last()