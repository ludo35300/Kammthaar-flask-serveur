
from services import influx_service
from services.authentification_service import Authentification
import requests



    
def get_last_batterie_data():
    return influx_service.get_last_data('battery_data')
    
def get_batterie_data_realtime():
        authentification_service = Authentification()
        try:
            # Effectuer la requête GET avec un délai de timeout
            response = authentification_service.get("/batterie/realtime")
            # Vérifier si la requête est réussie (statut HTTP 200)
            if response.status_code == 200:
                # Tenter de décoder le contenu JSON
                return response.json()  # Retourne directement les données JSON
            else:
                print(f"Erreur HTTP: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête: {e}")
            return None
        
def get_last_24h_pourcent():
    return influx_service.get_data_24h("battery_data", "battery_pourcent")
    
def get_last_24h_amperage():
    return influx_service.get_data_24h("battery_data", "battery_amperage")
    
def get_last_24h_voltage():
    return influx_service.get_data_24h("battery_data", "battery_voltage")
    
def get_last_24h_power():
    return influx_service.get_data_24h("battery_data", "battery_power")
    
def get_last_24h_temp():
    return influx_service.get_data_24h("battery_data", "battery_temp")
