# import requests
# import math
# from pprint import pprint


class Weather:

    city = 'Moscow'
    lang = 'RU'
    token_id = '82424742061e498492facc25c51dd408'
    api_key = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang={lang}&appid={token_id}&units=metric'

    def __init__(self):
        self._response = requests.get(self.api_key)
        self.info = self._response.json()
        self._min_temp = self.info['main']['temp_min']
        self._max_temp = self.info['main']['temp_max']
        self._pressure = self.info['main']['pressure']
        self._humidity = self.info['main']['humidity']
        self._wind_speed = self.info['wind']['speed']
        self._wind_deg = self.info['wind']['deg']
        self._weather_desc = self.info['weather'][0]['description']
        self._weather_main = self.info['weather'][0]['main']

    @property
    def innfo(self):
        return self.info

    @property
    def get_description(self):
        if self._weather_main == 'Clouds':
            self._weather_main = 'облачно'
        elif self._weather_main == 'Rain':
            self._weather_main = 'дождь'
        elif self._weather_main == 'Clear':
            self._weather_main = 'ясно'
        elif self._weather_main == 'Thunderstorm':
            self._weather_main = 'гроза'
        elif self._weather_main == 'Snow':
            self._weather_main = 'снег'
        elif self._weather_main == 'Mist':
            self._weather_main = 'туман'

        return f'Погода в москве: {self._weather_main}\n' \
               f'{self._weather_desc}, температура: {math.floor(self._min_temp)}-{math.floor(self._max_temp)}°C\n' \
               f'Давление: {self._pressure}мм рт. ст.,влажность: {self._humidity}%'


if __name__ == '__main__':
    moscow = Weather()
    pprint(moscow.info)
    #print(moscow.get_description)