from marshmallow import Schema, fields
    
class SolarDataSchema(Schema):
    voltage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la tension des panneaux solaire."})
    current = fields.Float(required=True, error_messages={"required": "Aucune donnée sur le courant des panneaux solaire."})
    power = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la puissance des panneaux solaire."})
    maximum_voltage_today = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la tension maximale des panneaux solaires aujourd'hui."})
    minimum_voltage_today = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la tension minimale des panneaux solaires aujourd'hui."}) 
    date = fields.DateTime(required=False, allow_none=True) # Champ 'date' optionnel
    
    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        
class Solar24hSchema(Schema):
    value = fields.Float(required=True, error_messages={"required": "Aucune donnée reçue de la batterie."})
    time = fields.DateTime(required=True) 

    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        

