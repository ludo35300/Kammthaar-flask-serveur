from flask import jsonify
from flask_smorest import Blueprint

from services import statistiques_service

statistiques_controller = Blueprint('statistiques_controller', __name__, url_prefix='/statistiques', description="")

@statistiques_controller.route('/last_statistiques', methods=['GET'])
def get_last_statistiques():
    return statistiques_service.get_last_statistiques()

@statistiques_controller.route('/realtime', methods=['GET'])
def get_statistiques_data_realtime():
    return statistiques_service.get_statistiques_data_realtime()