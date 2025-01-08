
from services import influx_service
from services.authentification_service import Authentification

def get_last_batterie_status_data():
    return influx_service.get_last_data('battery_status_data')
    
def get_batterie_status_data_realtime():
    authentification_service = Authentification()
    return authentification_service.get("/batterie/status/realtime")
        
    