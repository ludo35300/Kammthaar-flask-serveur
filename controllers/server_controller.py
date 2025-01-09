from flask import jsonify
from flask_smorest import Blueprint
from services.server_service import ServerService

server_controller = Blueprint('serveur', __name__, url_prefix='/serveur', description="Récupération des infos du serveur de Kammthaar")

@server_controller.route('/status', methods=['GET'])
def get_status():
    server_service = ServerService()
    return server_service.getStatus()

@server_controller.route('/infos', methods=['GET'])
def get_server_infos():
    server_service = ServerService()
    server_infos = server_service.get_server_infos()
    return server_infos.json()


    