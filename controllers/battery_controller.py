from flask import jsonify, request
from flask_smorest import Blueprint
from services import batterie_service
from services import batterie_status_service

batterie_controller = Blueprint('batterie_controller', __name__, url_prefix='/batterie', description="")

@batterie_controller.route('/last_batterie_data', methods=['GET'])
def get_last_battery_data():
    return batterie_service.get_last_batterie_data()

@batterie_controller.route('/last_status_data', methods=['GET'])
def get_last_battery_status_data():
    return batterie_status_service.get_last_batterie_status_data()


@batterie_controller.route('/batterie_realtime', methods=['GET'])
def get_battery_data_realtime():
    # Récupérer le verrou depuis `request.environ`
    mppt_lock = request.environ.get('mppt_lock', None)
    if not mppt_lock:
        return jsonify({"error": "MPPT lock is not configured"}), 500

    # Essayer d'acquérir le verrou
    if not mppt_lock.acquire(blocking=False):
        return jsonify({"error": "MPPT is busy, please try again later"}), 429
    try:
        # Lecture des données en temps réel
        batterie_realtime = batterie_service.get_batterie_data_realtime()
        # Vérifier si les données existent
        if batterie_realtime is None:
            return jsonify({"error": "No data found"}), 404
        # Retourner les données sous forme de JSON
        return batterie_realtime
    
    finally:
        # Libérer le verrou après traitement
        mppt_lock.release()

@batterie_controller.route('/status_realtime', methods=['GET'])
def get_battery_status_data_realtime():
    return batterie_status_service.get_batterie_status_data_realtime()



@batterie_controller.route('/last24hPourcent', methods=['GET'])
def last_24h_pourcent():
    return batterie_service.get_last_24h_pourcent()
    
@batterie_controller.route('/last24hAmperage', methods=['GET'])
def last_24h_amperage():
    return batterie_service.get_last_24h_amperage()
    
@batterie_controller.route('/last24hVoltage', methods=['GET'])
def last_24h_voltage():
    return batterie_service.get_last_24h_voltage()

@batterie_controller.route('/last24hPower', methods=['GET'])
def last_24h_power():
    return batterie_service.get_last_24h_power()
    
@batterie_controller.route('/last24hTemp', methods=['GET'])
def last_24h_temp():
    return batterie_service.get_last_24h_temp()