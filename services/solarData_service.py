
from dto.solarData_schema import SolarDataSchema
from entity.solarData_entity import SolarData
from services.authentification_service import Authentification
from services.influx_service import InfluxDbService


def get_realtime():
    """ Récupère les dernières données de la consommation en temps réel """
    try:
        params = Authentification().get("/solarData/realtime").json()
        solar_data = SolarData(
            voltage=params.get("voltage"),
            current=params.get("current"),
            power=params.get("power"),
            maximum_voltage_today=params.get("maximum_voltage_today"),
            minimum_voltage_today=params.get("minimum_voltage_today"),
            date=None
        )
        valid_data = SolarDataSchema().load(solar_data.to_dict())  # Valider et transformer en dict
        return valid_data
    except Exception as e:
        print("Erreur lors de la récupération des paramètres de SolarData en temps réel:", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None

def get_last():
    """ Récupère les dernières données enregistrées de la consommation dans influxDB"""
    try:
        params = InfluxDbService().get_last_data('solarData')
        # Mapper les paramètres récupérés vers un objet SolarData
        solar_data = SolarData(
            voltage=params.get("voltage"),
            current=params.get("current"),
            power=params.get("power"),
            maximum_voltage_today=params.get("maximum_voltage_today"),
            minimum_voltage_today=params.get("minimum_voltage_today"),
            date=params.get("date"),  # Ajoute la date si elle existe, sinon laisse None
        )
        valid_data = SolarDataSchema().load(solar_data.to_dict())  # Valider et transformer en dict
        return valid_data
    except Exception as e:
        print("Erreur lors de la récupération des derniers paramètres de SolarData :", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None