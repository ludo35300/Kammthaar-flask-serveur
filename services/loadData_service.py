from dto.loadData_schema import LoadDataSchema
from entity.loadData_entity import LoadData
from services.authentification_service import Authentification
from services.influx_service import InfluxDbService


def get_realtime():
    """ Récupère les dernières données de la consommation en temps réel """
    try:
        params = Authentification().get("/loadData/realtime").json()
        load_data = LoadData(
            voltage=params.get("voltage"),
            current=params.get("current"),
            power=params.get("power"),
            date=None
        )
        valid_data = LoadDataSchema().load(load_data.to_dict())  # Valider et transformer en dict
        return valid_data
    except Exception as e:
        print("Erreur lors de la récupération des paramètres de LoadData en temps réel:", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None

def get_last():
    """ Récupère les dernières données enregistrées de la consommation dans influxDB"""
    try:
        params = InfluxDbService().get_last_data('loadData')
        # Mapper les paramètres récupérés vers un objet LoadData
        load_data = LoadData(
            voltage=params.get("voltage"),
            current=params.get("current"),
            power=params.get("power"),
            date=params.get("date"),  # Ajoute la date si elle existe, sinon laisse None
        )
        valid_data = LoadDataSchema().load(load_data.to_dict())  # Valider et transformer en dict
        return valid_data
    except Exception as e:
        print("Erreur lors de la récupération des derniers paramètres de LoadData :", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None

def get_last_24h_data(column_name):
    """Récupère les données d'une colonne spécifique des dernières 24 heures"""
    return InfluxDbService().get_data_24h("loadData", column_name)