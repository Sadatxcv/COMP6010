item_to_locations = {
    "butter": "Aisle A",
    "bread": "Aisle B",
    "eggs": "Aisle A",
    "cereal": "Aisle B",
    "muesli": "Aisle B",
    "raisins": "Aisle C",
}

# Create a dictionary that maps from locations to lists of items
#
# e.g. {
#   "Aisle A": ["butter", "eggs"],
#   "Aisle B": ["bread", "cereal", "muesli"],
#   "Aisle C": ["raisins"],
# }

location_to_items = {}

for item in item_to_locations.keys():
    location = item_to_locations[item]

    if location not in location_to_items:
        location_to_items[location] = []

    location_to_items[location].append(item)

print(location_to_items)