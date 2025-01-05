from flask import jsonify
from constantes.constantes import Config
from models.battery_model import BatteryData
from models.battery_parametres_model import BatteryParametresData
from services.authentification_service import Authentification
from services.influx_service import InfluxService
import requests


class BatterieParametresService:
    def __init__(self):
        self.influx = InfluxService()
    
    def get_last_batterie_parametres_data(self):
        # Construire la requête pour récupérer les paramètres de batterie
        query = f'''
        from(bucket: "{Config.INFLUXDB_BUCKET}")
        |> range(start: -1d)   // Durée de recherche
        |> filter(fn: (r) => r._measurement == "batterie_parametres")
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
            battery_parametres_data = BatteryParametresData(
                rated_charging_current=params.get('rated_charging_current'),
                rated_load_current=params.get('rated_load_current'),
                real_rated_voltage=params.get('real_rated_voltage'),
                battery_type=params.get('battery_type'),
                battery_capacity=params.get('battery_capacity'),
                temp_compensation_coefficient=params.get('temp_compensation_coefficient'),
                over_voltage_disconnect=params.get('over_voltage_disconnect'),
                charging_limit_voltage=params.get('charging_limit_voltage'),
                over_voltage_reconnect=params.get('over_voltage_reconnect'),
                equalize_charging_voltage=params.get('equalize_charging_voltage'),
                boost_charging_voltage=params.get('boost_charging_voltage'),
                float_charging_voltage=params.get('float_charging_voltage'),
                boost_reconnect_voltage=params.get('boost_reconnect_voltage'),
                low_voltage_reconnect=params.get('low_voltage_reconnect'),
                under_voltage_recover=params.get('under_voltage_recover'),
                under_voltage_warning=params.get('under_voltage_warning'),
                low_voltage_disconnect=params.get('low_voltage_disconnect'),
                discharging_limit_voltage=params.get('discharging_limit_voltage'),
                battery_rated_voltage=params.get('battery_rated_voltage'),
                default_load_mode=params.get('equalize_duration'),
                equalize_duration=params.get('boost_charging_voltage'),
                boost_duration=params.get('boost_duration'),
                battery_discharge=params.get('battery_discharge'),
                battery_charge=params.get('battery_charge'),
                charging_mode=params.get('charging_mode'),
                battery_parametres_date=last_time
            )
            return jsonify(battery_parametres_data.to_dict())

        except Exception as e:
            print("Erreur lors de la récupération des paramètres de batterie :", e)

        # Si aucune donnée n'est trouvée ou en cas d'erreur
        return None
    
    def get_batterie_parametres_data_realtime(self):
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