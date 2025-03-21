from flask.views import MethodView
from flask_cors import CORS
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from dto.solarData_schema import Solar24hSchema, SolarDataSchema
from services import solarData_service




blp_domaine_externe = Blueprint("solarData_controller", "Données des panneaux solaires", url_prefix="/solarData", description="Récupération des données des panneaux solaires")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200", "https://app.kammthaar.fr"), supports_credentials=True)

@blp_domaine_externe.route('/realtime')
class SolarDataRealtime(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, SolarDataSchema())
    def get(self):
        """ 
        Récupère les dernières données des panneaux solaire en temps réel 
        -> Si système en ligne
        """
        return  solarData_service.get_realtime()

@blp_domaine_externe.route('/last')
class SolarDataLastRecord(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, SolarDataSchema())
    def get(self):
        """ 
        Récupère les dernières données des panneaux solaires enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return solarData_service.get_last()
    
@blp_domaine_externe.route('/last/24h/<string:data_type>')
class Last24hData(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, Solar24hSchema(many=True))
    def get(self, data_type):
        """ 
            Récupère toutes les valeurs d'une donnée spécifique enregistrées dans InfluxDB sur les dernières 24 heures ainsi que la date/heure de l'enregistrement.
        """
        valid_columns = ["voltage", "current", "power"]
        if data_type not in valid_columns:
            return {"erreur": f"'{data_type}' n'est pas un type de donnée valide."}, 400
        return solarData_service.get_last_24h_data(data_type)