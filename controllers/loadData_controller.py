from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint

from dto.loadData_schema import LoadDataSchema
from services import loadData_service


blp_domaine_externe = Blueprint("loadData_controller", "Données de consommation énergétique", url_prefix="/loadData", description="Récupération des données de consommation énergétique")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200"))

@blp_domaine_externe.route('/realtime')
class LoadDataRealtime(MethodView):
    @blp_domaine_externe.response(200, LoadDataSchema())
    def get(self):
        """ 
        Récupère les dernières données de la consommation en temps réel 
        -> Si système en ligne
        """
        return  loadData_service.get_realtime()

@blp_domaine_externe.route('/last')
class LoadDataLastRecord(MethodView):
    @blp_domaine_externe.response(200, LoadDataSchema())
    def get(self):
        """ 
        Récupère les dernières données de la consommation enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        return loadData_service.get_last()