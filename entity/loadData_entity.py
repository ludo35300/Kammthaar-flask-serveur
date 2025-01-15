from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Optional

@dataclass
class LoadData:
    voltage: float
    current: float
    power: float
    date: Optional[datetime]

    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour une sérialisation JSON."""
        data = asdict(self)
        if data.get('date'):
            data['date'] = data['date'].isoformat()  # Format ISO 8601
        return data