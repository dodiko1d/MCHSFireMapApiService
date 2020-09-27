import requests
import json
from sqlalchemy.orm import Session
from . import model

URL = 'http://maps.kosmosnimki.ru/rest/ver1/layers/F2840D287CD943C4B1122882C5B92565/search?query=%22DateTime%22%3E=%272020-08-07%27%20%20and%20%22DateTime%22%3C%272020-08-10%27%20&BorderFromLayer=78E56184F48149DF8A39BA81CA25A01E&BorderID=1&api_key=U26GSBBC7N&out_cs=EPSG:3395'


def overview_period(timestamp_1, timestamp_2):
    URL.replace(URL[URL.find('%27') + 3: URL.find('%27') + 13], timestamp_1)
    URL.replace(URL[URL.rfind('%27') - 12:URL.rfind('%27')], timestamp_2)
    return URL


def get_data():
    features = requests.get(URL).json()['features']
    return features


def fire_from_api(step, data):
    firepoint_id = data[step]['properties']['HotSpotId']
    lat = data[step]['properties']['latitude']
    long = data[step]['properties']['longitude']
    brightness = data[step]['properties']['brightness']
    probability = data[step]['properties']['Confidence']
    intensity = data[step]['properties']['Power']
    fire_type = data[step]['properties']['FireType']
    town = data[step]['properties']['Town']
    date_time = data[step]['properties']['DateTime']

    return model.FirePoint(firepoint_id, lat, long, brightness, probability, intensity, fire_type, town, date_time)
