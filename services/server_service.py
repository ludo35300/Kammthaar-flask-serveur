import os
import platform
import socket
import subprocess
from flask import jsonify
from constantes.constantes import Config
from services.authentification_service import Authentification


class ServerService:
    def is_raspberry_online(self):
        """ Vérifie si le Raspberry Pi est en ligne avec un ping. """
        adresse_ip = Config.IP_KAMMTHAAR
        port = 5001
        try:
            print(f"Trying to connect to {adresse_ip}:{port}")
            with socket.create_connection((adresse_ip, port), 2):
                print("Connection successful")
                return True
        except socket.timeout:
            print("Connection timed out")
            return False
        except OSError as e:
            print(f"OS error: {e}")
            return False

    def get_server_infos(self):
        try:
            response = Authentification().get("/serveur/infos")

            # Si la requête a échoué (timeout, erreur réseau, etc.)
            if response is False or response is None:
                return jsonify({"status": False, "message": "Raspberry Pi injoignable"}), 200

            # Vérifier si la réponse a un code HTTP valide
            if response.status_code != 200:
                return jsonify({"status": False, "message": f"Erreur {response.status_code} du Raspberry Pi"}), 200
            
            return response.json()
        
        except Exception as e:
            return jsonify({"status": False, "message": f"Erreur interne: {str(e)}"}), 500