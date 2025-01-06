from flask import jsonify
from flask_smorest import Blueprint

from services import batterie_parametres_service

batterie_parametres_controller = Blueprint('batterie_parametres_controller', __name__, url_prefix='/batterie_parametres', description="")

@batterie_parametres_controller.route('/last_batterie_parametres_data', methods=['GET'])
def get_last_batterie_parametres_data():
    return batterie_parametres_service.get_last_batterie_parametres_data()

@batterie_parametres_controller.route('/realtime', methods=['GET'])
def get_batterie_parametres_data_realtime():
    return batterie_parametres_service.get_batterie_parametres_data_realtime()