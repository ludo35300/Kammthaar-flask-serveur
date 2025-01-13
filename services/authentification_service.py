import requests
from constantes.constantes import Config

class Authentification:
    def __init__(self):
        self.token = None
        
        url = f"{Config.API_KAMMTHAAR}/authentification/login"
        payload = {"username": Config.USERNAME, "password": Config.MOT_DE_PASSE}
        try:
            response = requests.post(url, json=payload, timeout=5)
            response.raise_for_status()  # Vérifie si le statut HTTP indique une erreur
            self.token = response.json()["access_token"]
        except requests.ConnectTimeout:
            self.token = None  # Définit une valeur par défaut
        except requests.RequestException as e:
            self.token = None  # Définit une valeur par défaut
        # response = requests.post(url, json=payload, timeout=5)
        # if response.status_code == 200:
        #     self.token = response.json()["access_token"]
        # else:
        #     raise Exception("Erreur d'authentification")

    def get(self, endpoint):
        headers = {"Authorization": f"Bearer {self.token}"}
        url = f"{Config.API_KAMMTHAAR}{endpoint}"
        response = requests.get(url, headers=headers, timeout=5)
        return response

