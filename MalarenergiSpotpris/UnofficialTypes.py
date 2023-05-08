from dataclasses import dataclass, field
from typing import Any, List, Optional
from dataclasses_json import dataclass_json, config

@dataclass_json
@dataclass(frozen=True)
class Interval:
    """Interval data class"""
    interval: str = field(metadata=config(field_name="interval"))
    startDateTime: str = field(metadata=config(field_name="startDateTime"))
    endDateTime: str = field(metadata=config(field_name="endDateTime"))
    price: float = field(metadata=config(field_name="price"))

@dataclass_json
@dataclass(frozen=True)
class Base:
    """Base data class"""
    version: str = field(metadata=config(field_name="version"))
    area: str = field(metadata=config(field_name="area"))
    unit: str = field(metadata=config(field_name="unit"))
    currency: str = field(metadata=config(field_name="currency"))
    average: float = field(metadata=config(field_name="average"))
    current: Interval = field(metadata=config(field_name="current"))
    todayMin: Interval = field(metadata=config(field_name="todayMin"))
    todayMax: Interval = field(metadata=config(field_name="todayMax"))
    hasTomorrow: bool = field(metadata=config(field_name="hasTomorrow"))
    intervals: List[Interval] = field(metadata=config(field_name="intervals"))