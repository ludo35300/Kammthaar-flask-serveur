from flask.views import MethodView
from flask_cors import CORS
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from dto.breadcrumb_schema import BreadcrumbSchema
from services import breadcrumb_service

blp_domaine_externe = Blueprint("breadcrumb_controller", "Informations du breadcrumb", url_prefix="/breadcrumb", description="Récupération de l'heure et du status du jour")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200", "https://app.kammthaar.fr"), supports_credentials=True)

@blp_domaine_externe.route('/realtime')
class BreadcrumbRealtime(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, BreadcrumbSchema())
    def get(self):
        """ 
        Récupère les données du breadcrumb en temps réel
        """
        return  breadcrumb_service.get_realtime()
    
@blp_domaine_externe.route('/last')
class ChargingEquipmenLastRecord(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, BreadcrumbSchema())
    def get(self):
        """ 
        Récupère les dernières données de la batterie enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return breadcrumb_service.get_last()