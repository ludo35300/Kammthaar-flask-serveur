from flask import jsonify
from flask_smorest import Blueprint
from services.statistiques_service import StatistiquesService

statistiques_controller = Blueprint('statistiques_controller', __name__, url_prefix='/statistiques', description="")

@statistiques_controller.route('/last_statistiques', methods=['GET'])
def get_last_statistiques():
    statistiques_service = StatistiquesService()
    last_statistique = statistiques_service.get_last_statistiques()

    return jsonify(last_statistique)

@statistiques_controller.route('/realtime', methods=['GET'])
def get_statistiques_data_realtime():
    statistiques_service = StatistiquesService()
    statistiques_realtime = statistiques_service.get_statistiques_data_realtime()
    # Vérifier si les données existent
    if statistiques_realtime is None:
        return jsonify({"error": "No data found"}), 404
    # Retourner les données sous forme de JSON
    return statistiques_realtime