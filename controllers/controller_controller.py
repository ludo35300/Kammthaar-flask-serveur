from flask import jsonify, request
from flask_smorest import Blueprint

from services import controller_service

controller_controller = Blueprint('controller_controller', __name__, url_prefix='/controller', description="")

@controller_controller.route('/last', methods=['GET'])
def get_last_controller_data():
    return controller_service.get_last_controller_data()

@controller_controller.route('/realtime', methods=['GET'])
def get_controller_data_realtime():
    return controller_service.get_controller_data_realtime()

@controller_controller.route('/last24hVoltage', methods=['GET'])
def last_24h_voltage():
    # controller_service = ControllerService()
    return controller_service.get_last_24h_voltage()

@controller_controller.route('/last24hAmperage', methods=['GET'])
def last_24h_amperage():
    # controller_service = ControllerService()
    try:
        data_controller = controller_service.get_last_24h_amperage()
        if data_controller:
            return jsonify(data_controller)  # Renvoie les données sous forme JSON
        return jsonify({"error": "No data found"}), 404  # Aucune donnée trouvée
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@controller_controller.route('/last24hPower', methods=['GET'])
def last_24h_amperage():
    # controller_service = ControllerService()
    try:
        data_controller = controller_service.get_last_24h_power()
        if data_controller:
            return jsonify(data_controller)  # Renvoie les données sous forme JSON
        return jsonify({"error": "No data found"}), 404  # Aucune donnée trouvée
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@controller_controller.route('/last24hTemperature', methods=['GET'])
def last_24h_amperage():
    # controller_service = ControllerService()
    try:
        data_controller = controller_service.get_last_24h_temperature()
        if data_controller:
            return jsonify(data_controller)  # Renvoie les données sous forme JSON
        return jsonify({"error": "No data found"}), 404  # Aucune donnée trouvée
    except Exception as e:
        return jsonify({"error": str(e)}), 500