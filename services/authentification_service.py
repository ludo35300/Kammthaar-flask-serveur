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

    def get(self, endpoint):
        headers = {"Authorization": f"Bearer {self.token}"}
        url = f"{Config.API_KAMMTHAAR}{endpoint}"
        
        
        try:
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()  # Lève une exception si le code de statut HTTP indique une erreur
            
            # Si la réponse est un JSON, renvoyez directement le JSON
            return response  # Convertit la réponse JSON en dictionnaire Python
        except requests.ConnectTimeout:
            print(f"Timeout lors de la connexion à {url}. Serveur distant inaccessible.")
            return None  # Retourner False si un timeout se produit
        except requests.RequestException as e:
            print(f"Erreur de requête : {e}")
            return None
        
        # response = requests.get(url, headers=headers, timeout=5)
        # return response

