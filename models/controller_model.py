from dataclasses import asdict, dataclass
from datetime import datetime
from models.validators import Validators

@dataclass
class ControllerData:
    temperature: float
    amperage: float
    power: float
    voltage: float
    day_time: bool
    night_time: bool
    date: datetime
    
    def __post_init__(self):
        """Effectue les validations après l'initialisation."""
        self.temperature = Validators.validate_float(self.temperature, "controller_temperature")
        self.amperage = Validators.validate_float(self.amperage, "controller_load_amperage")
        self.power = Validators.validate_float(self.power, "controller_load_power")
        self.voltage = Validators.validate_float(self.voltage, "controller_load_voltage")
        self.day_time = Validators.validate_boolean(self.day_time, "controller_day_time")
        self.night_time = Validators.validate_boolean(self.night_time, "controller_night_time")
        self.date = Validators.validate_string(self.date, "controller_date")
        
    def to_dict(self):
        """Convertit l'objet en dictionnaire pour une sérialisation JSON."""
        data_dict = asdict(self)
        return data_dict