from marshmallow import Schema, fields

class BatteryDataDTO(Schema):
    def __init__(self, *args, **kwargs):
        self.battery_voltage = 0
        self.battery_amperage = 0
        self.battery_power = 0
        self.battery_temp = 0
        self.battery_pourcent = 0
        self.battery_time = None  # Ajout du champ time
        
        self.set_data(**kwargs)

    def set_data(self, **kwargs):
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
    
class BaseBatterySchema(Schema):
    __model__ = BatteryDataDTO
    battery_voltage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur le voltage de la batterie."})
    battery_amperage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'ampérage' de la batterie."})
    battery_power = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la puissance de la batterie de la batterie."})
    battery_temp = fields.Int(required=True, error_messages={"required": "Aucune donnée sur la température de la batterie."})
    battery_pourcent = fields.Int(required=True, error_messages={"required": "Aucune donnée sur le voltage de la batterie."})
    battery_time = fields.DateTime(required=False) 

    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"