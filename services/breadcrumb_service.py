
from dto.breadcrumb_schema import BreadcrumbSchema
from entity.breadcrumb_entity import Breadcrumb
from services.authentification_service import Authentification
from services.influx_service import InfluxDbService


def get_realtime():
    """ Récupère les dernières données du controller en temps réel """
    try:
        params = Authentification().get("/breadcrumb").json()
        breadcrumb = Breadcrumb(
            current_device_time = params.get("current_device_time"),
            day_time = params.get("day_time"),
        )
        return BreadcrumbSchema().load(breadcrumb.to_dict())  # retourne le breadcrum apres validation et transformation en dict
    except Exception as e:
        print("Erreur lors de la récupération des paramètres de controllerData en temps réel:", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None

def get_last():
    """ Récupère les dernières données enregistrées de la consommation dans influxDB"""
    try:
        # Mapper les paramètres récupérés vers un objet SolarData
        breadcrumb = Breadcrumb(
            current_device_time = InfluxDbService().get_last_data('controllerData').get("current_device_time"),
            day_time = InfluxDbService().get_last_data('dailyStatistics').get("day_time")
        )
        return BreadcrumbSchema().load(breadcrumb.to_dict())  # retourne le breadcrum apres validation et transformation en dict
    except Exception as e:
        print("Erreur lors de la récupération des derniers paramètres de SolarData :", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None