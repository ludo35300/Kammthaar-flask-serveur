from flask import jsonify
from flask_smorest import Blueprint
from services.server_service import ServerService

server_controller = Blueprint('server', __name__, url_prefix='/server', description="Récupération des infos du serveur de Kammthaar")

@server_controller.route('/status', methods=['GET'])
def get_status():
    server_service = ServerService()
    status = server_service.getStatus()

    # Vérifier si les données existent
    if status is False:
        return jsonify({"status": "false"}), 404
    else:
        return jsonify({"status": "true"}), 200

@server_controller.route('/infos_server', methods=['GET'])
def get_server_infos():
    server_service = ServerService()
    server_infos = server_service.get_server_infos()

    # Vérifier si les données existent
    if server_infos is None:
        return jsonify({"error": "No data found"}), 404

    # Retourner les données sous forme de JSON
    return server_infos


    