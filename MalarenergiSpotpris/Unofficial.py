#!/bin/env python3

import requests
from enum import Enum
from MalarenergiSpotpris.UnofficialTypes import Base


class Area(Enum):
    SE1 = "SE1"
    SE2 = "SE2"
    SE3 = "SE3"
    SE4 = "SE4"

class MalarenergiUnafficial:
    @staticmethod
    def get_area_price_info(area: Area) -> Base:
        r = requests.get("https://bff.malarenergi.se/spotpriser/api/v1/prices/area/{}".format(area.value))
        return Base.from_dict(r.json())