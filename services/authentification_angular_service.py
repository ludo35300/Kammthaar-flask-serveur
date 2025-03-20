from datetime import datetime

import jwt

from constantes.constantes import Config



def create_token(username):
        expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token valide 1h
        payload = {
            'username': username,
            'exp': expiration
        }
        return jwt.encode(payload, Config.TOKEN , algorithm='HS256')