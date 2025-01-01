class BatteryStatusData:
    def __init__(self, battery_inner_resistence_abnormal, battery_status, temperature_warning_status, wrong_identifaction_for_rated_voltage, battery_status_date):
        self.battery_inner_resistence_abnormal = battery_inner_resistence_abnormal
        self.battery_status = battery_status
        self.temperature_warning_status = temperature_warning_status
        self.wrong_identifaction_for_rated_voltage = wrong_identifaction_for_rated_voltage
        self.battery_status_date = battery_status_date
        
        
    def to_dict(self):
        """Convertir l'objet en dictionnaire pour sérialisation JSON."""
        return {
            "battery_inner_resistence_abnormal": self.battery_inner_resistence_abnormal,
            "battery_status": self.battery_status,
            "temperature_warning_status": self.temperature_warning_status,
            "wrong_identifaction_for_rated_voltage": self.wrong_identifaction_for_rated_voltage,
            "battery_status_date": self.battery_status_date
        }
    