from services import influx_service
from services.authentification_service import Authentification
import requests




    
def get_last_controller_data():
    return influx_service.get_last_data('controller_data')
        
def get_controller_data_realtime():
        authentification_service = Authentification()
        try:
            # Effectuer la requête GET avec un délai de timeout
            response = authentification_service.get("/mppt/realtime")
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
        
    # Récupère les données d'ampérage en Ampères du controller des dernières 24 heures  
def get_last_24h_amperage():
        data = influx_service.get_data_24h("controller_data", "amperage")
        return data
    
# Récupère les données de voltage en Volts du controller des dernières 24 heures
def get_last_24h_voltage():
        data = influx_service.get_data_24h("controller_data", "voltage")
        return data
    
    # Récupère les données de puissance en Watt des dernières 24 heures
def get_last_24h_power():
        data = influx_service.get_data_24h("controller_data", "power")
        return data
    
    # Récupère les dernières données de la température du controller des dernières 24 heures
def get_last_24h_temperature():
        data = influx_service.get_data_24h("controller_data", "temperature")
        return data
    