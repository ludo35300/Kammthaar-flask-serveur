import influxdb_client
from constantes.constantes import Config
from influxdb_client.client.write_api import SYNCHRONOUS



client = influxdb_client.InfluxDBClient(url=Config.INFLUXDB_URL, token=Config.INFLUXDB_TOKEN, org=Config.INFLUXDB_ORG)

        
def get_data_24h( measurement, field):
    try:
        query = f"""
            from(bucket: "{Config.INFLUXDB_BUCKET}")
                |> range(start: -1d)  // Dernières 24 heures
                |> filter(fn: (r) => r._measurement == "{measurement}")  // Filtrer par mesure
                |> filter(fn: (r) => r._field == "{field}")        // Filtrer par champ
            """
        # Exécuter la requête InfluxDB
        tables = client.query_api().query(org=Config.INFLUXDB_ORG, query=query)
        # Conversion des données en une liste compréhensible
        results = []
        for table in tables:
            for record in table.records:
                # Extraction des données pertinentes
                results.append({
                    "time": record.get_time(),       # Timestamp
                    "value": record.get_value(),     # Valeur
                })
        return results
    except Exception as e:
        print("Erreur lors de la récupération des paramètres sur 24H :", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None
    
def get_last_data( measurement):
    try:
        # Construire la requête pour récupérer les paramètres de batterie
        query = f'''
            from(bucket: "{Config.INFLUXDB_BUCKET}")
            |> range(start: -30d)   // Durée de recherche
            |> filter(fn: (r) => r._measurement == "{measurement}")
            |> last() 
            '''
        result = client.query_api().query(org=Config.INFLUXDB_ORG, query=query)
        # Initialiser un dictionnaire pour stocker les valeurs des paramètres
        params = {}
        # Parcourir tous les enregistrements pour remplir le dictionnaire des paramètres
        for table in result:
            for record in table.records:
                
                field = record.get_field()  # Nom du champ
                value = record.get_value()  # Valeur du champ
                params[field] = value
            params["date"] = record.get_time()
        return params
    except Exception as e:
        print("Erreur lors de la récupération des derniers paramètres de "+measurement+" :", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None
        