from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Dict, Optional

@dataclass
class DischargingEquipmentStatus:
    input_voltage_status: str
    output_power_load: str
    running: bool
    errors: Dict[str, bool]
    date: Optional[datetime]

    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour une sérialisation JSON."""
        data = asdict(self)
        if data.get('date'):
            data['date'] = data['date'].isoformat()  # Format ISO 8601
        return data
