from services import influx_service
from services.authentification_service import Authentification
        
def get_last():
    return influx_service.get_last_data('batterie_parametres')

def get_realtime():
    return Authentification().get("/batterie/parametres/realtime").json()