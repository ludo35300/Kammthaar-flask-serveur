from flask import jsonify
from flask.views import MethodView
from flask_cors import CORS
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from dto.raspberry_schema import BaseRaspberrySchema
from services.server_service import ServerService

blp_domaine_externe = Blueprint("serveur", "Serveur", url_prefix="/serveur", description="Récupération des infos du Raspberry de Kammthaar")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200", "https://app.kammthaar.fr"), supports_credentials=True)


@blp_domaine_externe.route('/status')
class ServeurStatus(MethodView):
    @blp_domaine_externe.response(200, any)
    def get(self):
        if ServerService().is_raspberry_online():
            return jsonify({"status": True, "message": "Raspberry Pi est en ligne"}), 200
        else:
            return jsonify({"status": False, "message": "Raspberry Pi est hors ligne"}), 200

@blp_domaine_externe.route('/infos')
class ServeurInfos(MethodView):
    @jwt_required()
    @blp_domaine_externe.response(200, BaseRaspberrySchema)
    def get(self):
        return ServerService().get_server_infos()


    