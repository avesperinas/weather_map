"""Module for extracting data from the Open-Meteo API."""

from typing import Dict, Any, Tuple

from .client import open_meteo_client
from weather_app.auxiliar.logging import manage_exception


def extract_current_weather_data(
    cities: Dict[str, Tuple[float, float]]
) -> Dict[str, Dict[str, Any]]:
    
    weather_data = {}
    for city, (latitude, longitude) in cities.items():

        api_response = open_meteo_client.get_current_weather_forecast(latitude, longitude)
        weather_data[city] = api_response

    return weather_data


@manage_exception
def extract_current_weather_for_city(
    latitude: float,
    longitude: float
) -> dict:
    
    return open_meteo_client.get_current_weather_forecast(latitude, longitude)
