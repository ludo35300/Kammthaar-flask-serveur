from models.controller_model import ControllerData
from services import influx_service
from services.authentification_service import Authentification
    
def get_last():
    """ Récupère les dernières données enregistrées du controller MPPT dans influxDB"""
    return influx_service.get_last_data('controller_data')
        
def get_realtime():
    """ Récupère les données du controller MPPT en temps réel """
    data : ControllerData = Authentification().get("/mppt/realtime").json()
    # print(data)
    return data

def get_last_24h_data(column_name):
    """Récupère les données d'une colonne spécifique des dernières 24 heures"""
    data : ControllerData = influx_service.get_data_24h("controller_data", column_name)
    print(data)
    return data

        