from flask import jsonify
from constantes.constantes import Config
import requests

from services.authentification_service import Authentification


class ServerService:
    def __init__(self):
        self.authentification_service = Authentification()
    
    def getStatus(self) -> bool:
        try:
            # response = requests.get(Config.API_KAMMTHAAR+"/status", timeout=5)  # Timeout pour éviter les blocages
            response = self.authentification_service.get("/serveur/status")
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def get_server_infos(self):
        try:
            # Effectuer la requête GET avec un délai de timeout
            response = self.authentification_service.get("/serveur/infos")
            
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