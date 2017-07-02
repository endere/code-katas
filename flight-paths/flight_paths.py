import json
from graph import Graph
with open('data.json') as data_file:
    data = json.load(data_file)
#json reader found at https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-using-python



def calculate_distance(point1, point2):  #pragma no cover
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3 # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])


    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934 # convert km to miles

def track_path(city1, city2, data=data):
    city_graph = Graph()
    location_dict = {}
    for city in data:
        try:
            location_dict[city['city']]
        except KeyError:
            location_dict[city['city']] = city['lat_lon']
    for city in data:
        for dest in city['destination_cities']:
            try:
                city_graph.add_edge(city['city'], dest, calculate_distance(city['lat_lon'], location_dict[dest]))
            except KeyError:
                pass
    try:
        return city_graph.bellman_ford(city1, city2)
    except KeyError:
        raise KeyError('City has no Latitude or Longitude Given.')

if __name__ == '__main__':
    print(track_path('London', 'Sydney'))
