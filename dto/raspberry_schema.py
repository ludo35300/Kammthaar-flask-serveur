from marshmallow import Schema, fields
    
class BaseRaspberrySchema(Schema):
    cpu_usage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'utilisation du CPU'."})
    disk_usage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'espace disque'."})
    memory_usage = fields.Float(required=True, error_messages={"required": "Aucune donnée sur l'utilisation de la RAM'."})
    temperature = fields.Float(required=True, error_messages={"required": "Aucune donnée sur la température du Rapberry."})

    # authorise les paramètres inconnus mais les efface
    class Meta:
        unknown = "exclude"
        