from datetime import datetime
from dto.batteryParameters_schema import BatteryParametersSchema
from entity.batteryParameters_entity import BatteryParameters
from services.authentification_service import Authentification
from services.influx_service import InfluxDbService

    

def get_realtime():
    """ Récupère les dernières données du controller en temps réel """
    try:
        params = Authentification().get("/battery/parameters/realtime").json()
        battery_parameters = BatteryParameters(
            rated_charging_current= params.get("rated_charging_current"),
            rated_load_current= params.get("rated_load_current"),
            real_rated_voltage= params.get("real_rated_voltage"),
            battery_type= params.get("battery_type"),
            battery_capacity= params.get("battery_capacity"),
            temp_compensation_coefficient= params.get("temp_compensation_coefficient"),
            over_voltage_disconnect= params.get("over_voltage_disconnect"),
            charging_limit_voltage= params.get("charging_limit_voltage"),
            over_voltage_reconnect= params.get("over_voltage_reconnect"),
            equalize_charging_voltage= params.get("equalize_charging_voltage"),
            boost_charging_voltage= params.get("boost_charging_voltage"),
            float_charging_voltage= params.get("float_charging_voltage"),
            boost_reconnect_voltage= params.get("boost_reconnect_voltage"),
            low_voltage_reconnect= params.get("low_voltage_reconnect"),
            under_voltage_recover= params.get("under_voltage_recover"),
            under_voltage_warning= params.get("under_voltage_warning"),
            low_voltage_disconnect= params.get("low_voltage_disconnect"),
            discharging_limit_voltage= params.get("discharging_limit_voltage"),
            battery_rated_voltage= params.get("battery_rated_voltage"),
            default_load_mode= params.get("default_load_mode"),
            equalize_duration= params.get("equalize_duration"),
            boost_duration= params.get("boost_duration"),
            battery_discharge= params.get("battery_discharge"),
            battery_charge= params.get("battery_charge"),
            charging_mode= params.get("charging_mode"),
            date=None
        )
        return battery_parameters
    except Exception as e:
        print("Erreur lors de la récupération des paramètres de BatteryParameters en temps réel:", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None

def get_last():
    """ Récupère les dernières données enregistrées du controlleur dans influxDB"""
    try:
        params = InfluxDbService().get_last_data('batteryParameters')
        # Mapper les paramètres récupérés vers un objet BatteryParameters
        battery_parameters = BatteryParameters(
            rated_charging_current= params.get("rated_charging_current"),
            rated_load_current= params.get("rated_load_current"),
            real_rated_voltage= params.get("real_rated_voltage"),
            battery_type= params.get("battery_type"),
            battery_capacity= params.get("battery_capacity"),
            temp_compensation_coefficient= params.get("temp_compensation_coefficient"),
            over_voltage_disconnect= params.get("over_voltage_disconnect"),
            charging_limit_voltage= params.get("charging_limit_voltage"),
            over_voltage_reconnect= params.get("over_voltage_reconnect"),
            equalize_charging_voltage= params.get("equalize_charging_voltage"),
            boost_charging_voltage= params.get("boost_charging_voltage"),
            float_charging_voltage= params.get("float_charging_voltage"),
            boost_reconnect_voltage= params.get("boost_reconnect_voltage"),
            low_voltage_reconnect= params.get("low_voltage_reconnect"),
            under_voltage_recover= params.get("under_voltage_recover"),
            under_voltage_warning= params.get("under_voltage_warning"),
            low_voltage_disconnect= params.get("low_voltage_disconnect"),
            discharging_limit_voltage= params.get("discharging_limit_voltage"),
            battery_rated_voltage= params.get("battery_rated_voltage"),
            default_load_mode= params.get("default_load_mode"),
            equalize_duration= params.get("equalize_duration"),
            boost_duration= params.get("boost_duration"),
            battery_discharge= params.get("battery_discharge"),
            battery_charge= params.get("battery_charge"),
            charging_mode= params.get("charging_mode"),
            date=params.get("date"),  # Ajoute la date si elle existe, sinon laisse None
        )
        return BatteryParametersSchema().load(battery_parameters.to_dict()) # Valider et transformer en dict
    except Exception as e:
        print("Erreur lors de la récupération des derniers paramètres de BatteryParameters :", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None