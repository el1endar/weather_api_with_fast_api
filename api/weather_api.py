from fastapi import APIRouter, Depends
from typing import Optional
from models.location import Location

from services.openweather_service import WeatherAPI

from utils import Loader


router = APIRouter()


@router.get('/api/weather/{city}')
def weather(loc: Location = Depends(),
            units: Optional[str] = 'metric'):

    data = WeatherAPI(
            apiKey=Loader.loadJson("config/config.json").get("apiKey")).\
            getReport(city=loc.city, state=loc.state,
                      country=loc.country, units=units
                      )

    return f"{loc.city}, {loc.state}, {loc.country}, in {units}"
