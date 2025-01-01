from flask import jsonify
from constantes.constantes import Config
from models.battery_status_model import BatteryStatusData
from services.influx_service import InfluxService
import requests


class BatterieStatusService:
    def __init__(self):
        self.influx = InfluxService()
    
    def get_last_batterie_status_data(self):
        # Construire la requête pour récupérer les paramètres du status de la batterie
        query = f'''
        from(bucket: "{Config.INFLUXDB_BUCKET}")
        |> range(start: -1d)   // Durée de recherche
        |> filter(fn: (r) => r._measurement == "battery_status_data")
        |> last() 
        '''

        try:
            result = self.influx.query_api.query(org=Config.INFLUXDB_ORG, query=query)
            # Initialiser un dictionnaire pour stocker les valeurs
            params = {}
            last_time = None  # Variable pour stocker l'horodatage de la dernière mesure
            # Parcourir tous les enregistrements pour remplir le dictionnaire des paramètres
            for table in result:
                for record in table.records:
                    field = record.get_field()  # Nom du champ
                    value = record.get_value()  # Valeur du champ
                    params[field] = value
                    last_time = record.get_time()
            print(params.get('battery_inner_resistence_abnormal'))
            # Construire l'objet BatteryStatusData
            battery_status_data = BatteryStatusData(
                battery_inner_resistence_abnormal=params.get('battery_inner_resistence_abnormal'),
                battery_status=params.get('battery_status'),
                temperature_warning_status=params.get('temperature_warning_status'),
                wrong_identifaction_for_rated_voltage=params.get('wrong_identifaction_for_rated_voltage'),
                battery_status_date=last_time
            )
            return jsonify(battery_status_data.to_dict())

        except Exception as e:
            print("Erreur lors de la récupération des paramètres de batterie :", e)

        # Si aucune donnée n'est trouvée ou en cas d'erreur
        return None
    
    def get_batterie_status_data_realtime(self):
        try:
            # Effectuer la requête GET avec un délai de timeout
            response = requests.get(Config.API_KAMMTHAAR+"/batterie/status", timeout=5)
            
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
        
    