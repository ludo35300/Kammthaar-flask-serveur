from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Optional

@dataclass
class EnergyStatistics:
    consumed_today: float
    consumed_this_month: float
    consumed_this_year: float
    total_consumed: float
    generated_today: float
    generated_this_month: float
    generated_this_year: float
    total_generated: float
    date: Optional[datetime]

    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour une sérialisation JSON."""
        data = asdict(self)
        if data.get('date'):
            data['date'] = data['date'].isoformat()  # Format ISO 8601
        return data