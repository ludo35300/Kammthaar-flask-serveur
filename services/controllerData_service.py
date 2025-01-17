
from datetime import datetime
from dto.controllerData_schema import ControllerDataSchema
from entity.controllerData_entity import ControllerData
from services.authentification_service import Authentification
from services.influx_service import InfluxDbService

    

def get_realtime():
    """ Récupère les dernières données du controller en temps réel """
    try:
        params = Authentification().get("/controller/realtime").json()
        current_device_date = datetime.strptime(params.get("current_device_time"), '%Y-%m-%dT%H:%M:%S')
        controller_data = ControllerData(
            current_device_time = current_device_date,
            device_over_temperature=params.get("device_over_temperature"),
            temperature=params.get("temperature"),
            date=None
        )
        return controller_data
    except Exception as e:
        print("Erreur lors de la récupération des paramètres de controllerData en temps réel:", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None

def get_last():
    """ Récupère les dernières données enregistrées du controlleur dans influxDB"""
    try:
        params = InfluxDbService().get_last_data('controllerData')
        # Mapper les paramètres récupérés vers un objet ControllerData
        controller_data = ControllerData(
            current_device_time=params.get("current_device_time"),
            device_over_temperature=params.get("device_over_temperature"),
            temperature=params.get("temperature"),
            date=params.get("date"),  # Ajoute la date si elle existe, sinon laisse None
        )
        controller_data_schema = ControllerDataSchema()   # Valider avec Marshmallow
        valid_data = controller_data_schema.load(controller_data.to_dict())  # Valider et transformer en dict
        return valid_data
    except Exception as e:
        print("Erreur lors de la récupération des derniers paramètres de controllerData :", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None