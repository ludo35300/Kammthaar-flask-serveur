import influxdb_client
from constantes.constantes import Config

client = influxdb_client.InfluxDBClient(url=Config.INFLUXDB_URL, token=Config.INFLUXDB_TOKEN, org=Config.INFLUXDB_ORG)
class InfluxDbService:   
    
    def get_data_24h(self, measurement, field):
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
        
    def get_last_data(self, measurement):
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
    
    
    def get_last_stats_journalier_7j(self):
        try:
            query = f'''
                from(bucket: "{Config.INFLUXDB_BUCKET}")
                |> range(start: -7d, stop: now()) 
                |> filter(fn: (r) => r["_measurement"] == "energyStatistics")
                |> filter(fn: (r) => r["_field"] == "generated_today" or r["_field"] == "consumed_today")

                |> aggregateWindow(every: 1d, offset: -3h, fn: last)
                |> yield(name: "last")
                '''

            result = client.query_api().query(org=Config.INFLUXDB_ORG, query=query)
            data = {}
            
            # Extraction des résultats
            for table in result:
                for record in table.records:
                    date_key = record.get_time().strftime("%Y-%m-%d")  # Regroupement par jour
                    if date_key not in data:
                        data[date_key] = {}
                    
                    # Ajoute la valeur au bon champ (consumed_today ou generated_today)
                    data[date_key][record.get_field()] = record.get_value()
  
            return data
        except Exception as e:
            print("Erreur lors de la récupération des 7 derniers jours des statistiques :", e)
        # Si aucune donnée n'est trouvée ou en cas d'erreur
        return None

    