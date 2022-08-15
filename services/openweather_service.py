from typing import Optional
import requests


class WeatherAPI(object):

    def __init__(self, apiKey: str):
        self.__apiKey = apiKey

    @property
    def apiKey(self):
        return self.__apiKey

    def getReport(self, city: str, state: Optional[str], country: str, units: str) -> dict:

        urlTemplate = "https://api.openweathermap.org/data/2.5/weather?" \
                      "lat={lat}&lon={lon}&appid={apiKey}"

        cityData = self.getCoordinates(city=city, country=country, state=state)

        url = urlTemplate.format(apiKey=self.apiKey,
                                 lat=cityData.get("lat"),
                                 lon=cityData.get("lon"))

        response = requests.get(url=url).json()
        print(f"RES: {response}")

        return dict()

    def getCoordinates(self, city: str, state: Optional[str], country: str) -> dict:

        q = "{city},{country}"

        if state:
            q = q + ",{state}"

        urlTemplate = f"https://api.openweathermap.org/geo/1.0/direct?q={q}" \
                      "&limit={limit}&appid={apiKey}"

        url = urlTemplate.format(city=city, state=state, country=country,
                                 limit=5, apiKey=self.apiKey)

        print(f"Coordinates url: {url}")

        response = requests.get(url=url).json()
        print(response)

        return response[0]
