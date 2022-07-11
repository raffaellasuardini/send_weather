import requests


class Weather:
    def __init__(self, endpoint, key, lat, lon):
        self.endpoint = endpoint
        self.parameters = {
            'lat': lat,
            'lon': lon,
            'appid': key,
            'exclude': 'current,minutely,alerts',
            'units': 'metric',
        }

    def getResponse(self):
        res = requests.get(url=self.endpoint, params=self.parameters)
        res.raise_for_status()
        weather_data = res.json()
        hours = weather_data["hourly"][:12]
        daily = weather_data["daily"][:3]

        # list of dict where every element is an hour
        hour_list = [{'dt': item["dt"],
                      'code': item["weather"][0]["id"],
                      'icon': item["weather"][0]["icon"]} for item in hours]

        # list of dict where every element is a day
        daily_list = [{
            'dt': item["dt"],
            'min': item["temp"]["min"],
            'max': item["temp"]["max"],
            'code': item["weather"][0]["id"],
            'icon': item["weather"][0]["icon"]
        } for item in daily]

        result = {
            'today': {
                'morning': hour_list[0],
                'afternoon': hour_list[6],
                'evening': hour_list[-1]
            },
            'next':{
                'one': daily_list[0],
                'two': daily_list[1],
                'three': daily_list[2]
            }
        }

        return result


