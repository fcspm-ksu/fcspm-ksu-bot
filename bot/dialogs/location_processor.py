from functools import reduce
import telegram
from .phrases import *
from .utils import *

SIMILARITY_THRESHOLD = 0.4


class LocationProcessor:
    locations = None
    as_dict = None

    specialities = []

    def __init__(self, obj: dict):
        self.locations = Location().deserialize(obj)
        self.as_dict = self.locations.flat()

    def similar(self, search: str):
        search = search.replace(WHERE_IS_PREFIX, '')
        keys = self.as_dict.keys()
        simirarity_weighted = lambda x: (similarity(search, x), x)
        weighted_names = [simirarity_weighted(x) for x in keys]
        sorted_names = sorted(weighted_names, key=lambda z: z[0])
        filtered_names = list(filter(lambda z: z[0] > SIMILARITY_THRESHOLD, sorted_names))
        return self.as_dict[filtered_names[-1][1]] if filtered_names else None

    def base(self):
        result = [self.locations]
        result.extend(self.locations.children)
        return result


class Location:
    name = None
    alt_names = []
    url = None
    description = None
    units = None
    longitude = None
    latitude = None
    specialities = []
    children = []

    @classmethod
    def deserialize(cls, json: dict):
        obj = cls()
        obj.__dict__ = json
        obj.children = [cls.inherit(c, obj) for c in obj.children]
        obj.children = [Location.deserialize(c) for c in obj.children]
        return obj

    @staticmethod
    def inherit(child: dict, parent: 'Location'):
        if not getattr(child, 'latitude', None) or not getattr(child, 'longitude', None):
            child['latitude'] = parent.latitude
            child['longitude'] = parent.longitude
        return child

    def map_link(self):
        return f"https://www.google.com/maps/place/{self.longitude},{self.latitude}/"

    def location(self):
        return telegram.Location(self.longitude, self.latitude)

    def formatted_units(self):
        msg = ''
        for unit in self.units:
            details = getattr(unit, 'details', None)
            msg += f'\n{unit["location"]}: {unit["name"]}' + (f' ({details})' if details else '')
        return msg

    def info(self):
        msg = f"{self.name}"
        msg += f"\n{self.url}" if self.url else ""
        msg += f"\n{self.description}" if self.description else ""
        msg += f"\n{self.formatted_units()}" if self.units else ""
        return msg

    def flat(self) -> dict:
        flatted = [{self.name: self}]
        flatted.extend([{alt_name: self} for alt_name in self.alt_names])
        flatted.extend([c.flat() for c in self.children])
        return reduce(lambda a, b: dict(a, **b), flatted)
