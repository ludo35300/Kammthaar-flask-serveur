

from constantes.constantes import Config
from services.authentification_service import Authentification
from services.influx_service import InfluxService
import requests


class StatistiquesService:
    def __init__(self):
        self.influx = InfluxService()
    
    def get_last_statistiques(self):
        # Construire la requête pour récupérer les paramètres de batterie
        query = f'''
        from(bucket: "{Config.INFLUXDB_BUCKET}")
        |> range(start: -1d)   // Durée de recherche
        |> filter(fn: (r) => r._measurement == "statistiques_data")
        |> last()
        '''
        try:
            # Exécuter la requête InfluxDB
            result = self.influx.query_api.query(org=Config.INFLUXDB_ORG, query=query)
            # Initialiser un dictionnaire pour stocker les valeurs des paramètres
            params = {}
            last_time = None  # Variable pour stocker l'horodatage de la dernière mesure
            # Parcourir tous les enregistrements pour remplir le dictionnaire des paramètres
            for table in result:
                for record in table.records:
                    field = record.get_field()  # Nom du champ
                    value = record.get_value()  # Valeur du champ
                    params[field] = value
                    last_time = record.get_time()
            params['last_measurement_time'] = last_time
           
            return params
        except Exception as e:
            print("Erreur lors de la récupération des paramètres des statistiques :", e)

        # Si aucune donnée n'est trouvée ou en cas d'erreur
        return None
    
    def get_statistiques_data_realtime(self):
        authentification_service = Authentification()
        try:
            response = authentification_service.get("/statistiques/realtime")
            
            # Vérifier si la requête est réussie (statut HTTP 200)
            if response.status_code == 200:
                return response.json()  # Retourne directement les données JSON
            else:
                print(f"Erreur HTTP: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête: {e}")
            return None