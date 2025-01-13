from dataclasses import dataclass, asdict
from models.validators import Validators  # Supposant que vous utilisez le même système de Validators.

@dataclass
class DischargerStatusData:
    boost_over_voltage: bool
    fault: bool
    input_over_voltage: bool
    input_voltage_status: str
    output_over_voltage: bool
    output_power_load: str
    output_voltage_abnormal: bool
    running: bool
    short_circuit: bool
    short_circuit_in_high_voltage_side: bool
    unable_to_discharge: bool
    unable_to_stop_discharging: bool

    def __post_init__(self):
        """Effectue les validations après l'initialisation."""
        self.boost_over_voltage = Validators.validate_boolean(self.boost_over_voltage, "boost_over_voltage")
        self.fault = Validators.validate_boolean(self.fault, "fault")
        self.input_over_voltage = Validators.validate_boolean(self.input_over_voltage, "input_over_voltage")
        self.input_voltage_status = Validators.validate_string(self.input_voltage_status, "input_voltage_status")
        self.output_over_voltage = Validators.validate_boolean(self.output_over_voltage, "output_over_voltage")
        self.output_voltage_abnormal = Validators.validate_string(self.output_voltage_abnormal, "output_voltage_abnormal")
        self.running = Validators.validate_boolean(self.running, "running")
        self.short_circuit = Validators.validate_boolean(self.short_circuit, "short_circuit")
        self.short_circuit_in_high_voltage_side = Validators.validate_boolean(self.short_circuit_in_high_voltage_side, "short_circuit_in_high_voltage_side")
        self.unable_to_discharge = Validators.validate_boolean(self.unable_to_discharge, "unable_to_discharge")
        self.unable_to_stop_discharging = Validators.validate_boolean(self.unable_to_stop_discharging, "unable_to_stop_discharging")

    def to_dict(self):
        """Convertit l'objet en dictionnaire pour une sérialisation JSON."""
        return asdict(self)
