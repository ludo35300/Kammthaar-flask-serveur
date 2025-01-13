from services import influx_service
from services.authentification_service import Authentification

def get_last():
    return influx_service.get_last_data('statistiques_data')
    
def get_realtime():
        return Authentification().get("/statistiques/realtime").json()