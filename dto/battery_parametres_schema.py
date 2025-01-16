from marshmallow import Schema, fields
    
class BaseBatteryParametresSchema(Schema):
    
    rated_charging_current = fields.Int(required=True, error_messages={"required": "Aucune donnée sur le voltage de la batterie."})
    rated_load_current = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'ampérage de la batterie."})
    real_rated_voltage = fields.Str(required=True, error_messages={"required": "Aucune donnée sur la puissance de la batterie."})
    battery_battery_type = fields.Str(required=True, error_messages={"required": "Aucune donnée sur la température de la batterie."})
    battery_capacity = fields.Int(required=True, error_messages={"required": "Aucune donnée sur le voltage de la batterie."})
    temp_compensation_coefficient = fields.Float(required=True, error_messages={"required": "Aucune donnée sur le coefficient de compensation de la temperature de la batterie."})
    over_voltage_disconnect = fields.Int(required=True, error_messages={"required": "Aucune donnée sur la déconnexion du voltage de la batterie."})
    charging_limit_voltage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la limite de charge de la batterie."})
    over_voltage_reconnect = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la reconnexion du voltage de la batterie."})
    equalize_charging_voltage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la charge d'égalisation de la batterie."})
    boost_charging_voltage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la charge de boost de la batterie."})
    float_charging_voltage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la charge flottante de la batterie."})
    boost_reconnect_voltage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la reconnexion de la charge de boost de la batterie."})
    low_voltage_reconnect = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la reconnexion du voltage de la batterie."})
    under_voltage_recover = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la récupération du voltage de la batterie."})
    under_voltage_warning = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'avertissement de voltage de la batterie."})
    low_voltage_disconnect = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la déconnexion du voltage de la batterie."})
    discharging_limit_voltage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la limite de décharge de la batterie."})
    battery_rated_voltage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur le voltage de la batterie."})
    default_load_mode = fields.Str(required=True, error_messages={"required": "Aucune donnée sur le mode de charge par défaut de la batterie."})
    equalize_duration = fields.Int(required=True, error_messages={"required": "Aucune donnée sur la durée d'égalisation de la batterie."})
    boost_duration = fields.Int(required=True, error_messages={"required": "Aucune donnée sur la durée de charge de boost de la batterie."})
    battery_discharge = fields.Int(required=True, error_messages={"required": "Aucune donnée sur la décharge de la batterie."})
    battery_charge = fields.Int(required=True, error_messages={"required": "Aucune donnée sur la charge de la batterie."})
    charging_mode = fields.Str(required=True, error_messages={"required": "Aucune donnée sur le mode de charge de la batterie."})
    
    time = fields.DateTime(required=False) 

    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        

class Value24hSchema(Schema):
    value = fields.Float(required=True, error_messages={"required": "Aucune donnée reçue de la batterie."})
    time = fields.DateTime(required=True) 

    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        