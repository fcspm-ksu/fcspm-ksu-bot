import json
import os

from .location_processor import LocationProcessor

data_path = os.environ.get('DATA_JSON_PATH', 'data.json')

with open(data_path) as f:
    data = json.load(f)

WHERE_IS = LocationProcessor(data['WHERE_IS'])
SPECIALITIES = data['SPECIALITIES']
COURSES = data['COURSES']
