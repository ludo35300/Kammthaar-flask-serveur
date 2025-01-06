from services import influx_service
from services.authentification_service import Authentification
import requests


        
def get_last_batterie_parametres_data():
    return influx_service.get_last_data('batterie_parametres')
        

def get_batterie_parametres_data_realtime():
        authentification_service = Authentification()
        try:
            response = authentification_service.get("/batterie/parametres/realtime")
            
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