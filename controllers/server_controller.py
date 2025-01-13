from flask.views import MethodView
from flask_cors import CORS
from flask_smorest import Blueprint
from dto.raspberry_schema import BaseRaspberrySchema
from services.server_service import ServerService

blp_domaine_externe = Blueprint("serveur", "Serveur", url_prefix="/serveur", description="Récupération des infos du Raspberry de Kammthaar")
CORS(blp_domaine_externe, origins=("http://localhost:4200" , "https://localhost:4200"))


@blp_domaine_externe.route('/status')
class ServeurStatus(MethodView):
    @blp_domaine_externe.response(200, any)
    def get(self):
        return ServerService().getStatus()

@blp_domaine_externe.route('/infos')
class ServeurInfos(MethodView):
    @blp_domaine_externe.response(200, BaseRaspberrySchema)
    def get(self):
        return ServerService().get_server_infos()


    