from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Dict, Optional

@dataclass
class BatteryStatus:
    voltage: float
    current: float
    power: float
    state_of_charge: int
    temperature: float
    # remote_temperature: float
    status: Dict[str, object]  # Statut détaillé de la batterie
    date: Optional[datetime]
    
    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour une sérialisation JSON."""
        data = asdict(self)
        if data.get('date'):
            data['date'] = data['date'].isoformat()  # Format ISO 8601
        return data