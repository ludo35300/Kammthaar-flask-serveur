from dto.energyStatistics_schema import EnergyStatisticsSchema
from entity.energyStatistics_entity import EnergyStatistics
from services.authentification_service import Authentification
from services.influx_service import InfluxDbService


def get_realtime():
    """ Récupère les dernières données du controller en temps réel """
    try:
        params = Authentification().get("/energy/statistiques/realtime").json()
        energy_statistics_data = EnergyStatistics(
            consumed_this_month=params.get("consumed_this_month"),
            consumed_this_year=params.get("consumed_this_year"),
            consumed_today=params.get("consumed_today"),
            generated_this_month=params.get("generated_this_month"),
            generated_this_year=params.get("generated_this_year"),
            generated_today=params.get("generated_today"),
            total_consumed=params.get("total_consumed"),
            total_generated=params.get("total_generated"),
            date=None
        )
        valid_data = EnergyStatisticsSchema().load(energy_statistics_data.to_dict())  # Valider et transformer en dict
        return valid_data
    except Exception as e:
        print("Erreur lors de la récupération des paramètres de EnergyStatistics en temps réel:", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None

def get_last():
    """ Récupère les dernières données enregistrées du controlleur dans influxDB"""
    try:
        params = InfluxDbService().get_last_data('energyStatistics')
        # Mapper les paramètres récupérés vers un objet EnergyStatistics
        energy_statistics_data = EnergyStatistics(
            consumed_this_month=params.get("consumed_this_month"),
            consumed_this_year=params.get("consumed_this_year"),
            consumed_today=params.get("consumed_today"),
            generated_this_month=params.get("generated_this_month"),
            generated_this_year=params.get("generated_this_year"),
            generated_today=params.get("generated_today"),
            total_consumed=params.get("total_consumed"),
            total_generated=params.get("total_generated"),
            date=params.get("date"),  # Ajoute la date si elle existe, sinon laisse None
        )
        valid_data = EnergyStatisticsSchema().load(energy_statistics_data.to_dict())  # Valider et transformer en dict
        return valid_data
    except Exception as e:
        print("Erreur lors de la récupération des derniers paramètres de EnergyStatistics :", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None