from marshmallow import Schema, fields
    
class BaseChargingStatusSchema(Schema):
    
    input_voltage_status= fields.Str(required=True, error_messages={"required": "Aucune donnée sur la température du contrôleur."})
    charging_mosfet_is_short_circuit = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur charging_mosfet_is_short_circuit."})
    charging_or_anti_reverse_mosfet_is_open_circuit = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur charging_or_anti_reverse_mosfet_is_open_circuit."})
    anti_reverse_mosfet_is_short_circuit = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur anti_reverse_mosfet_is_short_circuit."})
    input_over_current = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur load_over_current."})
    load_over_current = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur load_over_current."})
    load_short_circuit = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur load_short_circuit."})
    load_mosfet_short_circuit = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur load_mosfet_short_circuit."})
    disequilibrium_in_three_circuits = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur disequilibrium_in_three_circuits."})
    pv_input_short_circuit = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur pv_input_short_circuit."})
    charging_status = fields.Str(required=True, error_messages={"required": "Aucune donnée du status de chargement."})
    fault= fields.Boolean(required=True, error_messages={"required": "Aucune donnée s'il y a un défault."})
    running = fields.Boolean(required=True, error_messages={"required": "Aucune donnée si le controller MPPT est alummé."})
    
    date = fields.Str(required=False) 
    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        