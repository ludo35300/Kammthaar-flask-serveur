from flask import jsonify, request
from flask_smorest import Blueprint
from services.batterie_service import BatterieService
from services.batterie_status_service import BatterieStatusService

batterie_controller = Blueprint('batterie_controller', __name__, url_prefix='/batterie', description="")

@batterie_controller.route('/last_batterie_data', methods=['GET'])
def get_last_battery_data():
    batterie_service = BatterieService()
    last_batterie = batterie_service.get_last_batterie_data()

    # Vérifier si les données existent
    if last_batterie is None:
        return jsonify({"error": "No data found"}), 404

    # Retourner les données sous forme de JSON
    return last_batterie

@batterie_controller.route('/last_status_data', methods=['GET'])
def get_last_battery_status_data():
    batterie_status_service = BatterieStatusService()
    last_batterie_status = batterie_status_service.get_last_batterie_status_data()
 

    # Vérifier si les données existent
    if last_batterie_status is None:
        return jsonify({"error": "No data found"}), 404

    # Retourner les données sous forme de JSON
    return last_batterie_status


@batterie_controller.route('/batterie_realtime', methods=['GET'])
def get_battery_data_realtime():
    batterie_service = BatterieService()
    
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
    batterie_status_service = BatterieStatusService()
    status_realtime = batterie_status_service.get_batterie_status_data_realtime()

    # Vérifier si les données existent
    if status_realtime is None:
        return jsonify({"error": "No data found"}), 404

    # Retourner les données sous forme de JSON
    return status_realtime



@batterie_controller.route('/last24hPourcent', methods=['GET'])
def last_24h_pourcent():
    batterie_service = BatterieService()
    try:
        data_battery = batterie_service.get_last_24h_pourcent()
        if data_battery:
            return jsonify(data_battery)  # Renvoie les données sous forme JSON
        return jsonify({"error": "No data found"}), 404  # Aucune donnée trouvée
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@batterie_controller.route('/last24hAmperage', methods=['GET'])
def last_24h_amperage():
    batterie_service = BatterieService()
    try:
        data_battery = batterie_service.get_last_24h_amperage()
        if data_battery:
            return jsonify(data_battery)  # Renvoie les données sous forme JSON
        return jsonify({"error": "No data found"}), 404  # Aucune donnée trouvée
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@batterie_controller.route('/last24hVoltage', methods=['GET'])
def last_24h_voltage():
    batterie_service = BatterieService()
    try:
        data_battery = batterie_service.get_last_24h_voltage()
        if data_battery:
            return jsonify(data_battery)  # Renvoie les données sous forme JSON
        return jsonify({"error": "No data found"}), 404  # Aucune donnée trouvée
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@batterie_controller.route('/last24hPower', methods=['GET'])
def last_24h_power():
    batterie_service = BatterieService()
    try:
        data_battery = batterie_service.get_last_24h_power()
        if data_battery:
            return jsonify(data_battery)  # Renvoie les données sous forme JSON
        return jsonify({"error": "No data found"}), 404  # Aucune donnée trouvée
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@batterie_controller.route('/last24hTemp', methods=['GET'])
def last_24h_temp():
    batterie_service = BatterieService()
    try:
        data_battery = batterie_service.get_last_24h_temp()
        if data_battery:
            return jsonify(data_battery)  # Renvoie les données sous forme JSON
        return jsonify({"error": "No data found"}), 404  # Aucune donnée trouvée
    except Exception as e:
        return jsonify({"error": str(e)}), 500