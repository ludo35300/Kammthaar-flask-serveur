
from dto.dischargingEquipmentStatus_schema import DischargingEquipmentStatusSchema
from entity.dischargingEquipmentStatus_entity import DischargingEquipmentStatus
from services.authentification_service import Authentification
from services.influx_service import InfluxDbService

    

def get_realtime():
    """ Récupère les dernières données de la batterie en temps réel """
    try:
        params =  Authentification().get("/discharging/realtime").json()
        # discharging_equipment_status_data = DischargingEquipmentStatus(params)
        return params
    except Exception as e:
        print("Erreur lors de la récupération des paramètres de DischargingEquipmentStatus en temps réel:", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None

def get_last():
    """ Récupère les dernières données enregistrées de la batterie dans influxDB"""
    try:
        params = InfluxDbService().get_last_data('dischargingEquipmentStatus')
        print(params)
        # Mapper les paramètres récupérés vers un objet DischargingEquipmentStatusSchema
        discharging_equipment_status_data = DischargingEquipmentStatus(
            input_voltage_status = params.get("input_voltage_status"),
            output_power_load = params.get("output_power_load"),
            running = params.get("running"),
            date = params.get("date"),  # Ajoute la date si elle existe, sinon laisse None
            errors={
                "short_circuit": params.get("short_circuit"),
                "unable_to_discharge": params.get("unable_to_discharge"),
                "unable_to_stop_discharging": params.get("unable_to_stop_discharging"),
                "output_voltage_abnormal": params.get("output_voltage_abnormal"),
                "input_over_voltage": params.get("input_over_voltage"),
                "short_circuit_high_voltage_side": params.get("short_circuit_high_voltage_side"),
                "boost_over_voltage": params.get("boost_over_voltage"),
                "output_over_voltage": params.get("output_over_voltage"),
                "fault": params.get("fault")
            }
        )
        valid_data = DischargingEquipmentStatusSchema().load(discharging_equipment_status_data.to_dict())  # Valider avec marshmallow et transformer en dict
        return valid_data
    except Exception as e:
        print("Erreur lors de la récupération des derniers paramètres de dischargingEquipmentStatus :", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None