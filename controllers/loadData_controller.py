from flask.views import MethodView
from flask_cors import CORS
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from dto.loadData_schema import Load24hSchema, LoadDataSchema
from services import loadData_service


blp_domaine_externe = Blueprint("loadData_controller", "Données de consommation énergétique", url_prefix="/loadData", description="Récupération des données de consommation énergétique")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200", "https://app.kammthaar.fr"), supports_credentials=True)

@blp_domaine_externe.route('/realtime')
class LoadDataRealtime(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, LoadDataSchema())
    def get(self):
        """ 
        Récupère les dernières données de la consommation en temps réel 
        -> Si système en ligne
        """
        return  loadData_service.get_realtime()

@blp_domaine_externe.route('/last')
class LoadDataLastRecord(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, LoadDataSchema())
    def get(self):
        """ 
        Récupère les dernières données de la consommation enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return loadData_service.get_last()
    
@blp_domaine_externe.route('/last/24h/<string:data_type>')
class Last24hData(MethodView):
    @blp_domaine_externe.response(200, Load24hSchema(many=True))
    def get(self, data_type):
        """ 
            Récupère toutes les valeurs d'une donnée spécifique enregistrées dans InfluxDB sur les dernières 24 heures ainsi que la date/heure de l'enregistrement.
        """
        valid_columns = ["voltage", "current", "power"]
        if data_type not in valid_columns:
            return {"erreur": f"'{data_type}' n'est pas un type de donnée valide."}, 400
        return loadData_service.get_last_24h_data(data_type)