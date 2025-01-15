from dto.dailyStatistics_schema import DailyStatisticsSchema
from entity.dailyStatistics_entity import DailyStatistics
from services.authentification_service import Authentification
from services.influx_service import InfluxDbService


def get_realtime():
    """ Récupère les dernières données du controller en temps réel """
    try:
        params = Authentification().get("/statistiques/journalier/realtime").json()
        daily_statistics_data = DailyStatistics(
            maximum_battery_voltage_today=params.get("maximum_battery_voltage_today"),
            minimum_battery_voltage_today=params.get("minimum_battery_voltage_today"),
            day_time=params.get("day_time"),
            night_time=params.get("night_time"),
            date=None
        )
        return daily_statistics_data
    except Exception as e:
        print("Erreur lors de la récupération des paramètres de DailyStatistics en temps réel:", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None

def get_last():
    """ Récupère les dernières données enregistrées du controlleur dans influxDB"""
    try:
        params = InfluxDbService().get_last_data('dailyStatistics')
        # Mapper les paramètres récupérés vers un objet DailyStatistics
        daily_statistics_data = DailyStatistics(
            maximum_battery_voltage_today=params.get("maximum_battery_voltage_today"),
            minimum_battery_voltage_today=params.get("minimum_battery_voltage_today"),
            day_time=params.get("day_time"),
            night_time=params.get("night_time"),
            date=params.get("date"),  # Ajoute la date si elle existe, sinon laisse None
        )
        valid_data = DailyStatisticsSchema().load(daily_statistics_data.to_dict())  # Valider et transformer en dict
        return valid_data
    except Exception as e:
        print("Erreur lors de la récupération des derniers paramètres de DailyStatistics :", e)
    # Si aucune donnée n'est trouvée ou en cas d'erreur
    return None