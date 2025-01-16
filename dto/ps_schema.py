from marshmallow import Schema, fields
    
class BasePsSchema(Schema):
    voltage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur le voltage du panneau solaire."})
    amperage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'ampérage du panneau solaire."})
    power = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la puissance du panneau solaire."})
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
        