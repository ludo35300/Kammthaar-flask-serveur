from flask import jsonify
from services.authentification_service import Authentification


class ServerService:
    def __init__(self):
        self.authentification_service = Authentification()
    
    def getStatus(self) -> bool:
        server_service = ServerService()
        if server_service.authentification_service.token==None:
            return jsonify({"status": False}), 200
        else:
            return jsonify({"status": True}), 200 

    def get_server_infos(self):
        return self.authentification_service.get("/serveur/infos")