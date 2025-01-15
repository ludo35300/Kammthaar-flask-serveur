from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint

from dto.solarData_schema import SolarDataSchema
from services import solarData_service




blp_domaine_externe = Blueprint("solarData_controller", "Données des panneaux solaires", url_prefix="/solarData", description="Récupération des données des panneaux solaires")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200"))

@blp_domaine_externe.route('/realtime')
class SolarDataRealtime(MethodView):
    @blp_domaine_externe.response(200, SolarDataSchema())
    def get(self):
        """ 
        Récupère les dernières données des panneaux solaire en temps réel 
        -> Si système en ligne
        """
        return  solarData_service.get_realtime()

@blp_domaine_externe.route('/last')
class SolarDataLastRecord(MethodView):
    @blp_domaine_externe.response(200, SolarDataSchema())
    def get(self):
        """ 
        Récupère les dernières données des panneaux solaires enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return solarData_service.get_last()