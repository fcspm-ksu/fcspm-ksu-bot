import json
from environs import Env
from .location_processor import LocationProcessor


env = Env()
env.read_env(env.str('ENV_PATH', 'bot/env/dev.env'))
data_path = env.str('DATA_JSON_PATH', 'data.json')

with open(data_path) as f:
    data = json.load(f)

WHERE_IS = LocationProcessor(data['WHERE_IS'])
SPECIALITIES = data['SPECIALITIES']
COURSES = data['COURSES']
