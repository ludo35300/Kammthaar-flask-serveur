from flask import jsonify
from constantes.constantes import Config
from models.battery_model import BatteryData
from services.authentification_service import Authentification
from services.influx_service import InfluxService
import requests


class BatterieService:
    def __init__(self):
        self.influx = InfluxService()
    
    def get_last_batterie_data(self):
        # Construire la requête pour récupérer les paramètres de batterie
        query = f'''
        from(bucket: "{Config.INFLUXDB_BUCKET}")
        |> range(start: -1d)   // Durée de recherche
        |> filter(fn: (r) => r._measurement == "battery_data")
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
            battery_data = BatteryData(
                battery_amperage=params.get('battery_amperage'),
                battery_pourcent=params.get('battery_pourcent'),
                battery_power=params.get('battery_power'),
                battery_temp=params.get('battery_temp'),
                battery_voltage=params.get('battery_voltage'),
                battery_status=params.get('battery_status'),
                battery_date=last_time
            )
            return jsonify(battery_data.to_dict())

        except Exception as e:
            print("Erreur lors de la récupération des paramètres de batterie :", e)

        # Si aucune donnée n'est trouvée ou en cas d'erreur
        return None
    
    def get_batterie_data_realtime(self):
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
        
    def get_last_24h_pourcent(self):
        query = f"""
        from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -1d)  // Dernières 24 heures
            |> filter(fn: (r) => r._measurement == "battery_data")  // Filtrer par mesure
            |> filter(fn: (r) => r._field == "battery_pourcent")        // Filtrer par champ
        """
        data = self.influx.get_data_24h(query)
        return data
    
    def get_last_24h_amperage(self):
        query = f"""
        from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -1d)  // Dernières 24 heures
            |> filter(fn: (r) => r._measurement == "battery_data")  // Filtrer par mesure
            |> filter(fn: (r) => r._field == "battery_amperage")        // Filtrer par champ
        """
        data = self.influx.get_data_24h(query)
        return data
    
    def get_last_24h_voltage(self):
        query = f"""
        from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -1d)  // Dernières 24 heures
            |> filter(fn: (r) => r._measurement == "battery_data")  // Filtrer par mesure
            |> filter(fn: (r) => r._field == "battery_voltage")        // Filtrer par champ
        """
        data = self.influx.get_data_24h(query)
        return data
    
    def get_last_24h_power(self):
        query = f"""
        from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -1d)  // Dernières 24 heures
            |> filter(fn: (r) => r._measurement == "battery_data")  // Filtrer par mesure
            |> filter(fn: (r) => r._field == "battery_power")        // Filtrer par champ
        """
        data = self.influx.get_data_24h(query)
        return data
    
    def get_last_24h_temp(self):
        query = f"""
        from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -1d)  // Dernières 24 heures
            |> filter(fn: (r) => r._measurement == "battery_data")  // Filtrer par mesure
            |> filter(fn: (r) => r._field == "battery_temp")        // Filtrer par champ
        """
        data = self.influx.get_data_24h(query)
        return data
