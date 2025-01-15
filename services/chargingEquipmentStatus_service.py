from dto.chargingEquipmentStatus_schema import ChargingEquipmentStatusSchema
from entity.chargingEquipmentStatus_entity import ChargingEquipmentStatus
from services.authentification_service import Authentification
from services.influx_service import InfluxDbService

    

def get_realtime():
    """ Récupère les dernières données de la batterie en temps réel """
    return Authentification().get("/charging/realtime").json()

def get_last():
    """ Récupère les dernières données enregistrées de la batterie dans influxDB"""
    try:
        params = InfluxDbService().get_last_data('chargingEquipmentStatus')
        # Mapper les paramètres récupérés vers un objet ChargingEquipmentStatus
        charging_equipment_status_data = ChargingEquipmentStatus(
            input_voltage_status=params.get("input_voltage_status"),
            charging_status=params.get("charging_status"),
            running=params.get("running"),
            date=params.get("date"),  # Ajoute la date si elle existe, sinon laisse None
            errors={
                "charging_mosfet_short_circuit": params.get("charging_mosfet_short_circuit"),
                "charging_or_anti_reverse_mosfet_open_circuit": params.get("charging_or_anti_reverse_mosfet_open_circuit"),
                "anti_reverse_mosfet_short_circuit": params.get("anti_reverse_mosfet_short_circuit"),
                "input_over_current": params.get("input_over_current"),
                "load_over_current": params.get("load_over_current"),
                "load_short_circuit": params.get("load_short_circuit"),
                "load_mosfet_short_circuit": params.get("load_mosfet_short_circuit"),
                "disequilibrium_in_three_circuits": params.get("disequilibrium_in_three_circuits"),
                "pv_input_short_circuit": params.get("pv_input_short_circuit"),
                "fault": params.get("fault")
            }
        )
        valid_data = ChargingEquipmentStatusSchema().load(charging_equipment_status_data.to_dict())  # Valider et transformer en dict
        return valid_data
    except Exception as e:
        print("Erreur lors de la récupération des derniers paramètres de chargingEquipmentStatus :", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None