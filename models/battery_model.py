class BatteryData:
    def __init__(self, battery_voltage, battery_amperage, battery_power, battery_temp, battery_pourcent, battery_status, battery_date):
        self.battery_amperage = battery_amperage
        self.battery_voltage = battery_voltage
        self.battery_power = battery_power
        self.battery_temp = battery_temp
        self.battery_pourcent = battery_pourcent
        self.battery_status = battery_status
        self.battery_date = battery_date

    def to_dict(self):
        """Convertir l'objet en dictionnaire pour sérialisation JSON."""
        return {
            "battery_amperage": self.battery_amperage,
            "battery_voltage": self.battery_voltage,
            "battery_power": self.battery_power,
            "battery_temp": self.battery_temp,
            "battery_pourcent": self.battery_pourcent,
            "battery_status": self.battery_status,
            "battery_date": self.battery_date,
        }
    