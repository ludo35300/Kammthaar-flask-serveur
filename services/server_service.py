from flask import jsonify
from services.authentification_service import Authentification


class ServerService:
    def getStatus(self) -> bool:
        if Authentification().token==None:
            return jsonify({"status": False}), 200
        else:
            return jsonify({"status": True}), 200 

    def get_server_infos(self):
        return Authentification().get("/serveur/infos").json()