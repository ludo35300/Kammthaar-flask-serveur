from services import influx_service
from services.authentification_service import Authentification

def get_last():
    """ Récupère les dernières données enregistrées du panneau solaire dans influxDB"""
    return influx_service.get_last_data('ps_data')
    
def get_realtime():
    """ Récupère les données du panneau solaire en temps réel """
    return Authentification().get("/ps/realtime").json()

def get_last_24h_data(column_name):
    """Récupère les données d'une colonne spécifique des dernières 24 heures"""
    return influx_service.get_data_24h("ps_data", column_name)