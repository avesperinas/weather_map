"""Client module for interacting with the Open-Meteo API."""

import requests
import os

from weather_app.auxiliar.logging import manage_exception


class OpenMeteoAPIClient:

    def __init__(self):
        self.base_url = os.getenv("OPEN_METEO_API_BASE_URL")

    @manage_exception
    def _call_endpoint(
        self,
        endpoint: str,
        params: dict = None
    ) -> dict:
        
        response = requests.get(
            f"{self.base_url}{endpoint}",
            params=params
        )
        response.raise_for_status()
        return response.json()

    def get_current_weather_forecast(
        self,
        latitude: float,
        longitude: float,
    ) -> dict:
        
        return self._call_endpoint(
            endpoint="/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current_weather": "true",
                "models": "icon_eu",
                "timezone": "auto"
            }
        )
