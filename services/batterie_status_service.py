
from services import influx_service
from services.authentification_service import Authentification

def get_last_status():
    return influx_service.get_last_data('battery_status_data')
    
def get_status_realtime():
    return Authentification().get("/batterie/status/realtime").json()
        
    