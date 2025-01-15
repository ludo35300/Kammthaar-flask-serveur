from dto.batteryStatus_schema import BatteryStatusSchema
from entity.batteryStatus_entity import BatteryStatus
from services.authentification_service import Authentification
from services.influx_service import InfluxDbService

    

def get_realtime():
    """ Récupère les dernières données de la batterie en temps réel """
    return Authentification().get("/battery/realtime").json()

def get_last():
    """ Récupère les dernières données enregistrées de la batterie dans influxDB"""
    try:
        params = InfluxDbService().get_last_data('batteryStatus')
        # Mapper les paramètres récupérés vers un objet BatteryStatus
        battery_status_data = BatteryStatus(
            voltage=params.get("voltage"),
            current=params.get("current"),
            power=params.get("power"),
            state_of_charge=params.get("state_of_charge"),
            temperature=params.get("temperature"),
            date=params.get("date"),  # Ajoute la date si elle existe, sinon laisse None
            status={
                "battery_inner_resistence_abnormal": params.get("battery_inner_resistence_abnormal"),
                "wrong_identifaction_for_rated_voltage": params.get("wrong_identifaction_for_rated_voltage"),
                "temperature_warning_status": params.get("temperature_warning_status"),
                "battery_status": params.get("battery_status")
            }
            
        )
        battery_status_schema = BatteryStatusSchema()   # Valider avec Marshmallow
        valid_data = battery_status_schema.load(battery_status_data.to_dict())  # Valider et transformer en dict
        return valid_data
    except Exception as e:
        print("Erreur lors de la récupération des derniers paramètres de batteryStatus :", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None