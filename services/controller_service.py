from flask import jsonify
from constantes.constantes import Config
from models.controller_model import ControllerData
from services.authentification_service import Authentification
from services.influx_service import InfluxService
import requests


class ControllerService:
    def __init__(self):
        self.influx = InfluxService()
    
    def get_last_controller_data(self):
        # Construire la requête pour récupérer les paramètres de batterie
        query = f'''
        from(bucket: "{Config.INFLUXDB_BUCKET}")
        |> range(start: -1d)   // Durée de recherche
        |> filter(fn: (r) => r._measurement == "controller_data")
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
            # Construire l'objet ControllerData
            controller_data = ControllerData(
                controller_temperature=params.get('temperature'),
                controller_load_amperage=params.get('amperage'),
                controller_load_power=params.get('power'),
                controller_load_voltage=params.get('voltage'),
                controller_day_time=params.get('day_time'),
                controller_night_time=params.get('night_time'),
                controller_date=last_time
            )

            # Retourner l'objet sérialisé en JSON
            return jsonify(controller_data.to_dict())
        except Exception as e:
            print("Erreur lors de la récupération des données du contrôleur :", e)
            return jsonify({"error": "Erreur lors de la récupération des données"}), 500
        
    def get_controller_data_realtime(self):
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
    def get_last_24h_amperage(self):
        query = f"""
        from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -1d)  // Dernières 24 heures
            |> filter(fn: (r) => r._measurement == "controller_data")  // Filtrer par mesure
            |> filter(fn: (r) => r._field == "amperage")        // Filtrer par champ
        """
        data = self.influx.get_data_24h(query)
        return data
    
    # Récupère les données de voltage en Volts du controller des dernières 24 heures
    def get_last_24h_voltage(self):
        query = f"""
        from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -1d)  // Dernières 24 heures
            |> filter(fn: (r) => r._measurement == "controller_data")  // Filtrer par mesure
            |> filter(fn: (r) => r._field == "voltage")        // Filtrer par champ
        """
        data = self.influx.get_data_24h(query)
        return data
    
    # Récupère les données de puissance en Watt des dernières 24 heures
    def get_last_24h_power(self):
        query = f"""
        from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -1d)  // Dernières 24 heures
            |> filter(fn: (r) => r._measurement == "controller_data")  // Filtrer par mesure
            |> filter(fn: (r) => r._field == "power")        // Filtrer par champ
        """
        data = self.influx.get_data_24h(query)
        return data
    
    # Récupère les dernières données de la température du controller des dernières 24 heures
    def get_last_24h_temperature(self):
        query = f"""
        from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -1d)  // Dernières 24 heures
            |> filter(fn: (r) => r._measurement == "controller_data")  // Filtrer par mesure
            |> filter(fn: (r) => r._field == "temperature")        // Filtrer par champ
        """
        data = self.influx.get_data_24h(query)
        return data
    