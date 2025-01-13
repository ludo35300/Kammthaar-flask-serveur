from models.controller_model import ControllerData
from services import influx_service
from services.authentification_service import Authentification
    
def get_last():
    """ Récupère les dernières données enregistrées des informations de chargement dans influxDB"""
    return influx_service.get_last_data('charging_status_data')
        
def get_realtime():
    """ Récupère les données du controller MPPT en temps réel """
    return Authentification().get("/charging/status/realtime").json()


        