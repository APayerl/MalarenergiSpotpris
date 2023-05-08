# MalarenergiSpotpris
A small api wrapper to handle the complexity of getting the json and converting it to a typed object.

## Warning
Currently this uses a backward engineered API and could therefore break at any moment.

## Installation
```
pip install MalarenergiSpotpris
```

## Get started
How to use:

```Python
# At this point Mälarenergi does not have an official API.
from MalarenergiSpotpris import MalarenergiUnafficial as spot, Area

# Call with address
base = spot.get_area_price_info(Area.SE3)
print(base.current.price)  # Prints the current spot price
```