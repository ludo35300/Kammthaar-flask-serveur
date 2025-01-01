import influxdb_client
from constantes.constantes import Config
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxService:    
    def __init__(self):
        # Initialisation de la BDD InfluxDB
        self.client = influxdb_client.InfluxDBClient(url=Config.INFLUXDB_URL, token=Config.INFLUXDB_TOKEN, org=Config.INFLUXDB_ORG)
        self.query_api = self.client.query_api()
        
    def get_data_24h(self, query):
        # print(query)
        try:
            # Exécuter la requête InfluxDB
            tables = self.query_api.query(org=Config.INFLUXDB_ORG, query=query)

            # Conversion des données en une liste compréhensible
            results = []
            for table in tables:
                for record in table.records:
                    # Extraction des données pertinentes
                    results.append({
                        "time": record.get_time(),       # Timestamp
                        "value": record.get_value(),     # Valeur
                        "field": record.get_field(),     # Champ (amperage ici)
                        "measurement": record.get_measurement()  # Mesure (ps_data ici)
                    })
            return results

        except Exception as e:
            print("Erreur lors de la récupération des paramètres de batterie :", e)

        # Si aucune donnée n'est trouvée ou en cas d'erreur
        return None