class PSData:
    def __init__(self, ps_voltage, ps_amperage, ps_power, ps_date):
        self.ps_voltage = ps_voltage
        self.ps_amperage = ps_amperage
        self.ps_power = ps_power
        self.ps_date = ps_date

    def to_dict(self):
        """Convertir l'objet en dictionnaire pour sérialisation JSON."""
        return {
            "ps_voltage": self.ps_voltage,
            "ps_amperage": self.ps_amperage,
            "ps_power": self.ps_power,
            "ps_date": self.ps_date,
        }
