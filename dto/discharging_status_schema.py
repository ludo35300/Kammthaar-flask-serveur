from marshmallow import Schema, fields
    
class BaseDischargingStatusSchema(Schema):
    
    boost_over_voltage= fields.Boolean(required=True, error_messages={"required": "Aucune donnée sur la température du contrôleur."})
    fault = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur fault."})
    input_over_voltage = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur input_over_voltage"})
    input_voltage_status = fields.Str(required=True, error_messages={"required": "Aucune donnée du capteur input_voltage_status."})
    output_over_voltage = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur output_over_voltage."})
    output_power_load = fields.Str(required=True, error_messages={"required": "Aucune donnée du capteur output_power_load."})
    output_voltage_abnormal = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur output_voltage_abnormal."})
    running = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur running."})
    short_circuit = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur short_circuit."})
    short_circuit_in_high_voltage_side = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur short_circuit_in_high_voltage_side."})
    unable_to_discharge = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du status de unable_to_discharge."})
    unable_to_stop_discharging= fields.Boolean(required=True, error_messages={"required": "Aucune donnée unable_to_stop_discharging."})
    
    date = fields.Str(required=False) 
    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        