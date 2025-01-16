from marshmallow import Schema, fields
    
class BaseControllerSchema(Schema):
    temperature= fields.Float(required=True, error_messages={"required": "Aucune donnée sur la température du contrôleur."})
    voltage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur le voltage de la batterie."})
    amperage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'ampérage' de la batterie."})
    power = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la puissance de la batterie de la batterie."})
    day_time = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur si il fait jour."})
    night_time = fields.Boolean(required=True, error_messages={"required": "Aucune donnée du capteur si il fait nuit."})
    date = fields.Str(required=False) 
    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        

class Value24hSchema(Schema):
    value = fields.Float(required=True, error_messages={"required": "Aucune donnée reçue du controller MPPT."})
    time = fields.DateTime(required=True) 

    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        