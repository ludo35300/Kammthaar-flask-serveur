from flask.views import MethodView
from flask_cors import CORS
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from dto.dischargingEquipmentStatus_schema import DischargingEquipmentStatusSchema
from services import dischargingEquipmentStatus_service


blp_domaine_externe = Blueprint("dischargingEquipmentStatus_controller", "Status de la décharge", url_prefix="/discharging", description="Récupération des données du status de la décharge")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200", "https://app.kammthaar.fr"), supports_credentials=True)

@blp_domaine_externe.route('/realtime')
class DischargingEquipmentRealtime(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, DischargingEquipmentStatusSchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie en temps réel 
        -> Si système en ligne
        """
        return  dischargingEquipmentStatus_service.get_realtime()

@blp_domaine_externe.route('/last')
class DischargingEquipmentLastRecord(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, DischargingEquipmentStatusSchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return dischargingEquipmentStatus_service.get_last()