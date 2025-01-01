from flask import jsonify
from constantes.constantes import Config
from models.ps_model import PSData
from services.influx_service import InfluxService
import requests


class PsService:
    def __init__(self):
        self.influx = InfluxService()
    
    def get_last_ps_data(self):
        # Construire la requête pour récupérer les paramètres de batterie
        query = f'''
        from(bucket: "{Config.INFLUXDB_BUCKET}")
        |> range(start: -1d)   // Durée de recherche
        |> filter(fn: (r) => r._measurement == "ps_data")
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
            # Construire l'objet PSData
            ps_data = PSData(
                ps_voltage=params.get('voltage'),
                ps_amperage=params.get('amperage'),
                ps_power=params.get('power'),
                ps_date=last_time
            )
            return jsonify(ps_data.to_dict())

        except Exception as e:
            print("Erreur lors de la récupération des paramètres de batterie :", e)

        # Si aucune donnée n'est trouvée ou en cas d'erreur
        return None
    
    def get_ps_realtime(self):
        try:
            # Effectuer la requête GET avec un délai de timeout
            response = requests.get(Config.API_KAMMTHAAR+"/ps/realtime", timeout=5)
            
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
        
    def get_last_24h_amperage(self):
        query = f"""
        from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -1d)  // Dernières 24 heures
            |> filter(fn: (r) => r._measurement == "ps_data")  // Filtrer par mesure
            |> filter(fn: (r) => r._field == "amperage")        // Filtrer par champ
        """
        data = self.influx.get_data_24h(query)
        return data
    
    def get_last_24h_voltage(self):
        query = f"""
        from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -1d)  // Dernières 24 heures
            |> filter(fn: (r) => r._measurement == "ps_data")  // Filtrer par mesure
            |> filter(fn: (r) => r._field == "voltage")        // Filtrer par champ
        """
        data = self.influx.get_data_24h(query)
        return data
    
    def get_last_24h_power(self):
        query = f"""
        from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -1d)  // Dernières 24 heures
            |> filter(fn: (r) => r._measurement == "ps_data")  // Filtrer par mesure
            |> filter(fn: (r) => r._field == "power")        // Filtrer par champ
        """
        data = self.influx.get_data_24h(query)
        return data