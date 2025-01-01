from flask import jsonify
from flask_smorest import Blueprint
from services.ps_service import PsService

ps_controller = Blueprint('ps', __name__, url_prefix='/ps', description="")

@ps_controller.route('/last_ps_data', methods=['GET'])
def get_last_controller_data():
    ps_service = PsService()
    last_ps = ps_service.get_last_ps_data()

    # Vérifier si les données existent
    if last_ps is None:
        return jsonify({"error": "No data found"}), 404

    # Retourner les données sous forme de JSON
    return last_ps

@ps_controller.route('/realtime', methods=['GET'])
def get_ps_realtime():
    ps_service = PsService()
    ps_realtime = ps_service.get_ps_realtime()
    # Vérifier si les données existent
    if ps_realtime is None:
        return jsonify({"error": "No data found"}), 404
    # Retourner les données sous forme de JSON
    return ps_realtime

@ps_controller.route('/last24hVoltage', methods=['GET'])
def last_24h_voltage():
    ps_service = PsService()
    try:
        data_ps = ps_service.get_last_24h_voltage()
        if data_ps:
            return jsonify(data_ps)  # Renvoie les données sous forme JSON
        return jsonify({"error": "No data found"}), 404  # Aucune donnée trouvée
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@ps_controller.route('/last24hAmperage', methods=['GET'])
def last_24h_amperage():
    ps_service = PsService()
    try:
        data_ps = ps_service.get_last_24h_amperage()
        if data_ps:
            return jsonify(data_ps)  # Renvoie les données sous forme JSON
        return jsonify({"error": "No data found"}), 404  # Aucune donnée trouvée
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@ps_controller.route('/last24hPower', methods=['GET'])
def last_24h_amperage():
    ps_service = PsService()
    try:
        data_ps = ps_service.get_last_24h_power()
        if data_ps:
            return jsonify(data_ps)  # Renvoie les données sous forme JSON
        return jsonify({"error": "No data found"}), 404  # Aucune donnée trouvée
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    