import requests
from constantes.constantes import Config

class Authentification:
    def __init__(self):
        self.token = None
        
        url = f"{Config.API_KAMMTHAAR}/authentification/login"
        payload = {"username": Config.USERNAME, "password": Config.MOT_DE_PASSE}
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            self.token = response.json()["access_token"]
        else:
            raise Exception("Erreur d'authentification")

    def get(self, endpoint):
        headers = {"Authorization": f"Bearer {self.token}"}
        url = f"{Config.API_KAMMTHAAR}{endpoint}"
        response = requests.get(url, headers=headers, timeout=5)
        return response
