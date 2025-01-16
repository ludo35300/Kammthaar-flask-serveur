from marshmallow import Schema, fields
    
class BaseStatistiquesSchema(Schema):
    max_battery_voltage_today = fields.Float(required=True, error_messages={"required": "Aucune donnée sur le voltage du panneau solaire."})
    min_battery_voltage_today = fields.Float(required=True, error_messages={"required": "Aucune donnée sur le voltage de la  batterie minimum."})
    max_ps_voltage_today = fields.Float(required=True, error_messages={"required": "Aucune donnée sur le voltage du panneau solaire maximum."})
    min_ps_voltage_today = fields.Float(required=True, error_messages={"required": "Aucune donnée sur le voltage du panneau solaire minimum."})
    consumed_energy_today = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'énergie consommée aujourd'hui."})
    consumed_energy_month = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'énergie consommée ce mois."})
    consumed_energy_year = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'énergie consommée cette année."})
    consumed_energy_total = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'énergie consommée totale."})
    generated_energy_today = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'énergie générée aujourd'hui."})
    generated_energy_month = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'énergie générée ce mois."})
    generated_energy_year = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'énergie générée cette année."})
    generated_energy_total = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'énergie générée totale."})
    time = fields.DateTime(required=False) 

    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        

        