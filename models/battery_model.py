from dataclasses import dataclass
from datetime import datetime, time

@dataclass(frozen=True) # Lecture seule
class BatteryData:
    battery_voltage: float
    battery_amperage: float
    battery_power: float
    battery_temp: float
    battery_pourcent: int
    battery_time: time

    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour une sérialisation JSON."""
        return {
            "battery_voltage": self.battery_voltage,
            "battery_amperage": self.battery_amperage,
            "battery_power": self.battery_power,
            "battery_temp": self.battery_temp,
            "battery_pourcent": self.battery_pourcent,
            "battery_time": self.battery_time,
            
        }