# import requests
# import math
# import re
# from pprint import pprint


class Weather5Day:

    token_id = '82424742061e498492facc25c51dd408'
    lat = 55.7504461
    lon = 37.6174943
    api_key = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={token_id}&units=metric'

    def __init__(self):
        self._response = requests.get(self.api_key)
        self.info = self._response.json()
        self.first_day_night = self.info['list'][2]['main']['temp_max']
        self.first_day = self.info['list'][4]['main']['temp_max']
        self.first_day_icon = self.info['list'][2]['weather'][0]['icon']
        self.second_day = self.info['list'][12]['main']['temp_max']
        self.second_day_night = self.info['list'][16]['main']['temp_max']
        self.second_day_icon = self.info['list'][12]['weather'][0]['icon']
        self.third_day_night = self.info['list'][8]['main']['temp_max']
        self.third_day_ = self.info['list'][14]['main']['temp_max']
        self.third_day_icon = self.info['list'][14]['weather'][0]['icon']
        self.fourth_day_night = self.info['list'][26]['main']['temp_max']
        self.fourth_day = self.info['list'][20]['main']['temp_max']
        self.fourth_day_icon = self.info['list'][20]['weather'][0]['icon']
        self.fifth_day_night = self.info['list'][34]['main']['temp_max']
        self.fifth_day = self.info['list'][28]['main']['temp_max']
        self.fifth_day_icon = self.info['list'][28]['weather'][0]['icon']
        self.date_1 = self.info['list'][1]['dt_txt']
        self.date_2 = self.info['list'][37]['dt_txt']
        self.list_icons = [self.first_day_icon, self.second_day_icon, self.third_day_icon, self.fourth_day_icon, self.fifth_day_icon]
        self.image = f'weather_icons/{" ".join(self.list_icons)}.png'

        #self._min_temp = self.second_day['list'][12]['main']['temp_min']
        self._max_temp = self.info['list'][12]['main']['temp_max']
        self._pressure = self.info['list'][12]['main']['pressure']
        self._humidity = self.info['list'][12]['main']['humidity']
        self._wind_speed = self.info['list'][12]['wind']['speed']
        self._wind_deg = self.info['list'][12]['wind']['deg']
        self._weather_desc = self.info['list'][12]['weather'][0]['description']
        self._weather_main = self.info['list'][12]['weather'][0]['main']

    @property
    def get_info(self):
        return f''\
               f'Погода по Москве {self.date_1[:10]}-{self.date_2[:10]}\n'\
               f'/ {self.first_day}°C // {self.second_day}°C // {self.third_day_}°C\
                // {self.fourth_day}°C // {self.fifth_day}°C / ДЕНЬ\n' \
               f'/ {self.first_day_night}°C // {self.second_day_night}°C // {self.third_day_night}°C\
                // {self.fourth_day_night}°C // {self.fifth_day_night}°C / НОЧЬ'

    @property
    def get_info_tomorrow(self):
        return f'Погода в москве: {self.second_day}\n' \
               f'{self._weather_desc}, температура: {math.floor(self._max_temp)}-{math.floor(self._max_temp)}°C\n' \
               f'Давление: {self._pressure}мм рт. ст.,влажность: {self._humidity}%'

    def index(self):
        return self.pattern_1, self.pattern_2

if __name__ == '__main__':
    f = Weather5Day()
    #pprint(f.info)
    print(f.get_info_tomorrow)