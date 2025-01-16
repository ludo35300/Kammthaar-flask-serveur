from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Optional

@dataclass
class SolarData:
    voltage: float
    current: float
    power: float
    maximum_voltage_today: float
    minimum_voltage_today: float
    date: Optional[datetime]

    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour une sérialisation JSON."""
        data = asdict(self)
        if data.get('date'):
            data['date'] = data['date'].isoformat()  # Format ISO 8601
        return data