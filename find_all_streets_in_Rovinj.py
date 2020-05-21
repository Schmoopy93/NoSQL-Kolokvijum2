from pymongo import MongoClient
import json

client = MongoClient(port=27017)
db = client['croatia_osm']
cities_collection = db['cities']
streets_collection = db['streets']

center_point = {'lat': 45.0812, 'lon': 13.6387}
cities_cursor = cities_collection.find()
cities_list = list(cities_cursor)
cities_clean = []

for city in cities_list:
    cities_clean.append({'name': city['name']})

with open('cities.json', 'w') as file:
    json.dump(cities_clean, file)

streets_cursor = streets_collection.find()
streets_list = list(streets_cursor)
streets_within = []

for street in streets_list:
    if(street['city'] == 'Rovinj'):
            print(street)
            streets_within.append(
                {'city': street['city'], 'street': street['street']})

with open('streetsInRovinj.json', 'w') as file:
    json.dump(streets_within, file)
