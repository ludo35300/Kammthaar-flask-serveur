from dataclasses import asdict, dataclass
from datetime import datetime
from models.validators import Validators

@dataclass
class PSData:
    voltage: float
    amperage: float
    ps_power: float
    
    def __post_init__(self):
        """Effectue les validations après l'initialisation."""
        self.voltage = Validators.validate_int(self.voltage, "ps_voltage")
        self.amperage = Validators.validate_float(self.amperage, "ps_amperage")
        self.power = Validators.validate_float(self.power, "ps_power")
        
    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour une sérialisation JSON."""
        return asdict(self)
    
@dataclass
class Value24h:
    value: float
    time: datetime

    def __post_init__(self):
        """Effectue les validations après l'initialisation."""
        self.value = Validators.validate_float(self.value, "value")
        self.ps_time = Validators.validate_string(self.time, "time")

    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour une sérialisation JSON."""
        return asdict(self)
