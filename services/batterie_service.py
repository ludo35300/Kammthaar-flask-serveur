from services import influx_service
from services.authentification_service import Authentification

    
def get_last_data():
    return influx_service.get_last_data('battery_data')
    
def get_batterie_data_realtime():
        authentification_service = Authentification()
        return authentification_service.get("/batterie/realtime")

def get_last_24h_data(column_name):
    """Récupère les données d'une colonne spécifique des dernières 24 heures"""
    return influx_service.get_data_24h("battery_data", column_name)

# def get_last_24h():
#     return influx_service.get_24h("battery_data")
        
# def get_last_24h_pourcent():
#     return influx_service.get_data_24h("battery_data", "battery_pourcent")
    
# def get_last_24h_amperage():
#     return influx_service.get_data_24h("battery_data", "battery_amperage")
    
# def get_last_24h_voltage():
#     return influx_service.get_data_24h("battery_data", "battery_voltage")
    
# def get_last_24h_power():
#     return influx_service.get_data_24h("battery_data", "battery_power")
    
# def get_last_24h_temp():
#     return influx_service.get_data_24h("battery_data", "battery_temp")
