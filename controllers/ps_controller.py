from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint
from dto.battery_schema import Value24hSchema
from dto.ps_schema import BasePsSchema
from services import ps_service

blp_domaine_externe = Blueprint('ps', "Panneau solaire", url_prefix='/ps', description="Récupération des données du panneau solaire")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200"))


@blp_domaine_externe.route('/realtime')
class ControllerRealtime(MethodView):
    @blp_domaine_externe.response(200, BasePsSchema())
    def get(self):
        """ 
        Récupère les données du panneau solaire en temps réel 
        -> Si système en ligne
        """
        print(ps_service.get_realtime())
        return  ps_service.get_realtime()
    
@blp_domaine_externe.route('/last')
class ControllerLastRecord(MethodView):
    @blp_domaine_externe.response(200, BasePsSchema())
    def get(self):
        """ 
        Récupère les dernières données du panneau solaire enregistrées dans InfluxDB
        -> Si système hors ligne
        """
        print(ps_service.get_last())
        return ps_service.get_last()
    
@blp_domaine_externe.route('/last/24h/<string:data_type>')
class Last24hData(MethodView):
    @blp_domaine_externe.response(200, Value24hSchema(many=True))
    def get(self, data_type):
        """ 
            Récupère toutes les valeurs d'une donnée spécifique enregistrées dans InfluxDB sur les dernières 24 heures ainsi que la date/heure de l'enregistrement.
        """
        valid_columns = ["voltage", "amperage", "power", "temperature"]
        if data_type not in valid_columns:
            return {"erreur": f"'{data_type}' n'est pas un type de donnée valide."}, 400
        return ps_service.get_last_24h_data(data_type)