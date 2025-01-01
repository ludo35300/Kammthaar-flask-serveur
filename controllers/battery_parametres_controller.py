from flask import jsonify
from flask_smorest import Blueprint
from services.batterie_parametres_service import BatterieParametresService

batterie_parametres_controller = Blueprint('batterie_parametres_controller', __name__, url_prefix='/batterie_parametres', description="")

@batterie_parametres_controller.route('/last_batterie_parametres_data', methods=['GET'])
def get_last_batterie_parametres_data():
    batterie_parametres_service = BatterieParametresService()
    last_batterie = batterie_parametres_service.get_last_batterie_parametres_data()

    # Vérifier si les données existent
    if last_batterie is None:
        return jsonify({"error": "No data found"}), 404

    # Retourner les données sous forme de JSON
    return last_batterie

@batterie_parametres_controller.route('/realtime', methods=['GET'])
def get_batterie_parametres_data_realtime():
    batterie_parametres_service = BatterieParametresService()
    batterie_parametres_realtime = batterie_parametres_service.get_batterie_parametres_data_realtime()

    # Vérifier si les données existent
    if batterie_parametres_realtime is None:
        return jsonify({"Erreur": "Aucune donnée trouvée"}), 404

    # Retourner les données sous forme de JSON
    return batterie_parametres_realtime