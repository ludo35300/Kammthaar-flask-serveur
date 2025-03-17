
from datetime import  datetime, timedelta, timezone
from flask import jsonify, make_response, request
from flask_cors import CORS
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, set_access_cookies, set_refresh_cookies, unset_jwt_cookies
from flask_smorest import Blueprint
import jwt
from constantes.constantes import Config


blp_domaine_externe = Blueprint("authentification_controller", "Authentification", description="Fonction d'authentification")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200", "https://app.kammthaar.fr"), supports_credentials=True)

@blp_domaine_externe.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # Validation de l'utilisateur 
     

    if username != Config.USERNAME_ANGULAR and password != Config.MOT_DE_PASSE_ANGULAR :
        return jsonify({"msg": "Identifiants incorrects"}), 401

    access_token = create_access_token(identity=username, additional_claims={"username": username}, expires_delta=timedelta(hours=10))
    refresh_token = create_refresh_token(identity=username)

    response = make_response(jsonify({"message": "Connexion réussie"}))

    # Définir le cookie avec SameSite=None et Secure=True
    response.set_cookie('access_token_cookie', access_token, httponly=True, samesite='None', secure=True, max_age=36000)
    response.set_cookie('refresh_token_cookie', refresh_token, httponly=True, samesite='None', secure=True, max_age=360000)
    # Ajout des cookies à la réponse
    return response

@blp_domaine_externe.route('/server-time')
def get_server_time():
    utc_time = datetime.now(timezone.utc)
    return {"server_time": utc_time.isoformat()}

# Endpoint de rafraîchissement du token
@blp_domaine_externe.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)   # Nécessite un refresh token
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    
    response = jsonify({"msg": "Token rafraîchi"})
    set_access_cookies(response, new_access_token)
    return response

# Déconnexion (efface les cookies)
@blp_domaine_externe.route("/logout", methods=["POST"])
def logout():
    response = make_response({'message': 'Déconnexion réussie'}, 200)
    response.delete_cookie('access_token_cookie', path='/', samesite='None', secure=True)
    response.delete_cookie('refresh_token_cookie', path='/', samesite='None', secure=True)
    return response

@blp_domaine_externe.route('/check_auth', methods=['GET'])
def check_auth():
    # Vérifie si le cookie d'authentification est présent
    token = request.cookies.get('access_token_cookie')
    if token:
        # Vérification du token (exemple : validité ou décodage du JWT)
        if is_valid_token(token):  #fonction pour valider le token
            return jsonify({'authenticated': True})
    return jsonify({'authenticated': False})

# Fonction pour valider le token 
def is_valid_token(token):
    # Validation du token avec un secret ou décodage JWT
    try:
        decoded_token = decode_jwt(token)
        if decoded_token:
            return True
    except Exception:
        return False
    return False

def decode_jwt(token):
    """
    Décode le JWT et renvoie les données qu'il contient.
    Si le token est invalide ou expiré, lève une exception.
    """
    try:
        # Décoder le JWT avec la clé secrète
        payload = jwt.decode(token, Config.TOKEN, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token expiré."}, 401
    except jwt.InvalidTokenError:
        return {"error": "Token invalide."}, 401
    
def get_authenticated_user():
    """Récupérer l'utilisateur depuis le token JWT."""
    token = request.cookies.get('access_token_cookie')  # Récupérer le token JWT dans les cookies
    if not token:
        return None
    
    try:
        # Décoder le token pour extraire l'info utilisateur
        decoded_token = jwt.decode(token, Config.TOKEN, algorithms=["HS256"])
        # Retourner le dictionnaire avec les informations de l'utilisateur
        return decoded_token
    except jwt.ExpiredSignatureError:
        return None  # Token expiré
    except jwt.InvalidTokenError:
        return None  # Token invalide

# Exemple d'utilisation dans une route
@blp_domaine_externe.route('/user', methods=['GET'])
def get_user_info():
    user = get_authenticated_user()
    if user:
        # Accéder au nom d'utilisateur via la clé 'username' du dictionnaire
        return jsonify({'username': user['username']}), 200
    else:
        return jsonify({'message': 'User not authenticated'}), 401