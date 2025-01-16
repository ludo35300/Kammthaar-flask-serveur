from marshmallow import Schema, fields
    
class BaseBatterySchema(Schema):
    battery_voltage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur le voltage de la batterie."})
    battery_amperage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'ampérage' de la batterie."})
    battery_power = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la puissance de la batterie."})
    battery_temp = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la température de la batterie."})
    battery_pourcent = fields.Int(required=True, error_messages={"required": "Aucune donnée sur le voltage de la batterie."})
    battery_time = fields.DateTime(required=False) 

    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        

class Value24hSchema(Schema):
    value = fields.Float(required=True, error_messages={"required": "Aucune donnée reçue de la batterie."})
    time = fields.DateTime(required=True) 

    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        