from marshmallow import Schema, fields
    
class BaseBatteryStatusSchema(Schema):
    wrong_identifaction_for_rated_voltage = fields.Bool(required=True, error_messages={"required": "Aucune donnée sur l'identification du voltage de la batterie."})
    battery_inner_resistence_abnormal = fields.Bool(required=True, error_messages={"required": "Aucune donnée sur la résistance interne de la batterie."})
    temperature_warning_status = fields.Str(required=True, error_messages={"required": "Aucune donnée sur l'indication de la temperature de la batterie."})
    battery_status = fields.Str(required=True, error_messages={"required": "Aucune donnée sur le status de la batterie."})
    battery_status_time = fields.DateTime(required=False) 

    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        
        