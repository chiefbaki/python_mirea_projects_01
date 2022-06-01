import requests
from math import floor
from PIL import Image
from urllib.request import urlopen


class TomorrowWeather:

    api_key = f'http://api.openweathermap.org/data/2.5/forecast?q=moscow,ru&APPID=3051c8da538a2e104685783dae4796f4&units=metric&lang=ru'

    def __init__(self):
        self._response = requests.get(self.api_key)
        self._info = self._response.json()
        # Температура
        self.morning_temp_max = str(floor(int(self._info['list'][7]['main']['temp_max'])))  # 09:00
        self.afternoon_temp_max = str(floor(int(self._info['list'][9]['main']['temp_max'])))  # 15:00
        self.evening_temp_max = str(floor(int(self._info['list'][10]['main']['temp_max'])))  # 18:00
        self.night_temp_max = str(floor(int(self._info['list'][11]['main']['temp_max'])))  # 21:00
        # Иконки
        self.morning_icon = self._info['list'][7]['weather'][0]['icon']
        self.afternoon_icon = self._info['list'][9]['weather'][0]['icon']
        self.evening_icon = self._info['list'][10]['weather'][0]['icon']
        self.night_icon = self._info['list'][11]['weather'][0]['icon']

    def morning(self):
        morning_temp = str(int(self._info['list'][7]['main']['temp_min'])) + '-' + str(int(self._info['list'][7]['main']['temp_max']))
        morning_desc = self._info['list'][7]['weather'][0]['description']
        # Влажность
        morning_humid = self._info['list'][7]['main']['humidity']
        # Давление
        morning_pressure = str(int(float(self._info['list'][7]['main']['pressure']) / 1.33))
        # Ветер
        morning_wind_speed = self._info['list'][7]['wind']['speed']
        morning_wind_slug = self._get_wind_slug(float(morning_wind_speed)).lower()
        morning_wind_deg_slug = self._get_wind_deg_slug(morning_wind_speed)

        return f'Утро\n{morning_desc}, температура: {morning_temp}℃\n'\
               f'Давление: {morning_pressure} мм рт. ст., влажность: {morning_humid}%\n'\
               f'Ветер: {morning_wind_slug}, {morning_wind_speed} м/c, {morning_wind_deg_slug}\n'

    def afternoon(self):
        afternoon_temp = str(int(self._info['list'][9]['main']['temp_min'])) + '-' + str(int(self._info['list'][9]['main']['temp_max']))
        afternoon_desc = self._info['list'][9]['weather'][0]['description']
        afternoon_humid = self._info['list'][9]['main']['humidity']
        afternoon_pressure = str(int(float(self._info['list'][9]['main']['pressure']) / 1.33))
        afternoon_wind_speed = self._info['list'][9]['wind']['speed']
        afternoon_wind_slug = self._get_wind_slug(float(afternoon_wind_speed)).lower()
        afternoon_wind_deg_slug = self._get_wind_deg_slug(afternoon_wind_speed)

        return f'День\n{afternoon_desc}, температура: {afternoon_temp}℃\n' \
               f'Давление: {afternoon_pressure} мм рт. ст., влажность: {afternoon_humid}%\n' \
               f'Ветер: {afternoon_wind_slug}, {afternoon_wind_speed} м/c, {afternoon_wind_deg_slug}\n'

    def evening(self):
        evening_temp = str(int(self._info['list'][10]['main']['temp_min'])) + '-' + str(int(self._info['list'][10]['main']['temp_max']))
        evening_desc = self._info['list'][10]['weather'][0]['description']
        evening_humid = self._info['list'][10]['main']['humidity']
        evening_pressure = str(int(float(self._info['list'][10]['main']['pressure']) / 1.33))
        evening_wind_speed = self._info['list'][10]['wind']['speed']
        evening_wind_slug = self._get_wind_slug(float(evening_wind_speed)).lower()
        evening_wind_deg_slug = self._get_wind_deg_slug(evening_wind_speed)

        return f'Вечер\n{evening_desc}, температура: {evening_temp}℃\n' \
               f'Давление: {evening_pressure} мм рт. ст., влажность: {evening_humid}%\n' \
               f'Ветер: {evening_wind_slug}, {evening_wind_speed} м/c, {evening_wind_deg_slug}\n'


    def night(self):
        night_temp = str(int(self._info['list'][11]['main']['temp_min'])) + '-' + str(int(self._info['list'][11]['main']['temp_max']))
        night_desc = self._info['list'][11]['weather'][0]['description']
        night_humid = self._info['list'][11]['main']['humidity']
        night_pressure = str(int(float(self._info['list'][11]['main']['pressure']) / 1.33))
        night_wind_speed = self._info['list'][7]['wind']['speed']
        night_wind_slug = self._get_wind_slug(float(night_wind_speed)).lower()
        night_wind_deg_slug = self._get_wind_deg_slug(night_wind_speed)

        return f'Ночь\n{night_desc}, температура: {night_temp}℃\n' \
               f'Давление: {night_pressure} мм рт. ст., влажность: {night_humid}%\n' \
               f'Ветер: {night_wind_slug}, {night_wind_speed} м/c, {night_wind_deg_slug}\n'


    @property
    def get_weather_tomorrow(self):
        return f'{self.morning()}\n'\
               f'{self.afternoon()}\n' \
               f'{self.evening()}\n' \
               f'{self.night()}\n' \

    @property
    def get_info(self):
        return self._info

    def _get_wind_slug(self, speed: float) -> str:
        """
        Возвращает словесное название  ветра по шкале Бофорта
        """
        s = 'Ураган'
        if speed <= 0.2:
            s = 'Штиль'
        elif speed <= 1.5:
            s = 'Тихий'
        elif speed <= 3.3:
            s = 'Лёгкий'
        elif speed <= 5.4:
            s = 'Слабый'
        elif speed <= 7.9:
            s = 'Умеренный'
        elif speed <= 10.7:
            s = 'Свежий'
        elif speed <= 13.8:
            s = 'Сильный'
        elif speed <= 17.1:
            s = 'Крепкий'
        elif speed <= 20.7:
            s = 'Очень крепкий'
        elif speed <= 24.4:
            s = 'Шторм'
        elif speed <= 28.4:
            s = 'Сильный шторм'
        elif speed <= 32.6:
            s = 'Жестокий шторм'
        return s

    def _get_wind_deg_slug(self, deg: int) -> str:
        """
        Возращает буквенное направление ветра
        """
        s = 'северный'
        if deg <= 22.5:
            s = 'северный'
        elif deg <= 67.5:
            s = 'северо-восточный'
        elif deg <= 112.5:
            s = 'восточный'
        elif deg <= 157.5:
            s = 'юго-восточный'
        elif deg <= 202.5:
            s = 'южный'
        elif deg <= 247.5:
            s = 'юго-западный'
        elif deg <= 292.5:
            s = 'западный'
        elif deg <= 292.5:
            s = 'северо-западный'
        return s


    def show_pic(self):
        image = Image.new('RGBA', (400, 100), 'blue')
        img = image.resize((400, 100))
        im = Image.open(urlopen(f'https://openweathermap.org/img/wn/{self.morning_icon}@2x.png'))
        img.paste(im, (0, 0))
        im = Image.open(urlopen(f'https://openweathermap.org/img/wn/{self.afternoon_icon}@2x.png'))
        img.paste(im, (100, 0))
        im = Image.open(urlopen(f'https://openweathermap.org/img/wn/{self.evening_icon}@2x.png'))
        img.paste(im, (200, 0))
        im = Image.open(urlopen(f'https://openweathermap.org/img/wn/{self.night_icon}@2x.png'))
        img.paste(im, (300, 0))
        img.save('data/weather_tom.png')

class Weather5Day:

    api_key = f'http://api.openweathermap.org/data/2.5/forecast?q=moscow,ru&APPID=3051c8da538a2e104685783dae4796f4&units=metric&lang=ru'

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
        self.third_day = self.info['list'][14]['main']['temp_max']
        self.third_day_icon = self.info['list'][14]['weather'][0]['icon']
        self.fourth_day_night = self.info['list'][26]['main']['temp_max']
        self.fourth_day = self.info['list'][20]['main']['temp_max']
        self.fourth_day_icon = self.info['list'][20]['weather'][0]['icon']
        self.fifth_day_night = self.info['list'][34]['main']['temp_max']
        self.fifth_day = self.info['list'][28]['main']['temp_max']
        self.fifth_day_icon = self.info['list'][28]['weather'][0]['icon']
        self.date_1 = self.info['list'][1]['dt_txt']
        self.date_2 = self.info['list'][9]['dt_txt']
        self.date_3 = self.info['list'][17]['dt_txt']
        self.date_4 = self.info['list'][25]['dt_txt']
        self.date_5 = self.info['list'][37]['dt_txt']
        self._max_temp = self.info['list'][12]['main']['temp_max']
        self._pressure = self.info['list'][12]['main']['pressure']
        self._humidity = self.info['list'][12]['main']['humidity']
        self._wind_speed = self.info['list'][12]['wind']['speed']
        self._wind_deg = self.info['list'][12]['wind']['deg']
        self._weather_desc = self.info['list'][12]['weather'][0]['description']
        self._weather_main = self.info['list'][12]['weather'][0]['main']

    def show_pic(self):
        image = Image.new('RGBA', (500, 100), 'blue')
        im = Image.open(urlopen(f'https://openweathermap.org/img/wn/{self.first_day_icon}@2x.png'))
        image.paste(im, (0, 0))
        im = Image.open(urlopen(f'https://openweathermap.org/img/wn/{self.second_day_icon}@2x.png'))
        image.paste(im, (100, 0))
        im = Image.open(urlopen(f'https://openweathermap.org/img/wn/{self.third_day_icon}@2x.png'))
        image.paste(im, (200, 0))
        im = Image.open(urlopen(f'https://openweathermap.org/img/wn/{self.fourth_day_icon}@2x.png'))
        image.paste(im, (300, 0))
        im = Image.open(urlopen(f'https://openweathermap.org/img/wn/{self.fifth_day_icon}@2x.png'))
        image.paste(im, (400, 0))
        image.save('data/weather_5day.png')

    @property
    def get_info(self):
        return f''\
               f'Погода по Москве с {self.date_1[:10]} по {self.date_2[:10]}\n\n'\
               f'Погода на {self.date_1[:10]}:\n\
                Днем: {self.first_day}°C, Ночью: {self.first_day_night}°C\n\n' \
               f'Погода на {self.date_2[:10]}:\n\
                Днем: {self.second_day}°C, Ночью: {self.second_day_night}°C\n\n' \
               f'Погода на {self.date_3[:10]}:\n\
                Днем: {self.third_day}°C, Ночью: {self.third_day_night}°C\n\n' \
               f'Погода на {self.date_4[:10]}:\n\
                Днем: {self.fourth_day}°C, Ночью: {self.fourth_day_night}°C\n\n'\
               f'Погода на {self.date_5[:10]}:\n\
                Днем: {self.fifth_day}°C, Ночью: {self.fifth_day_night}°C\n'\

    @property
    def get_info_tomorrow(self):
        return f'Погода в москве: {self.second_day}\n' \
               f'{self._weather_desc}, температура: {floor(self._max_temp)}-{floor(self._max_temp)}°C\n' \
               f'Давление: {self._pressure}мм рт. ст.,влажность: {self._humidity}%'
