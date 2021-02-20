import googlemaps
from os import environ
from datetime import datetime
from sys import stdout
from itertools import combinations


NOW = datetime.now()


def API_request(mode, names, api_key):
    '''
    Arguments: 
        mode: mode of transportation, is supplied to the API
        names: list of names of the pubs
    Returns:
        - Travel distance and duration between each pair of pubs
        - Symmetric matrix of travel duration between each pair of pubs
        - Symmetric matrix of travel distance between each pair of pubs
    '''
    gmaps = googlemaps.Client(key=api_key)
    # To save on the number of requests to the API, only one way between each
    # pairs of locations is considered. It might be that the traveling distance
    # and duration differs if we go the other way but I assume this is negligable.
    pairs = list(combinations(names, 2))
    durations = []
    distances = []
    for _ in range(len(names)):
        durations.append([0]*len(names))
        distances.append([0]*len(names))
    for (i, (name1, name2)) in enumerate(pairs):
        f_name1 = 'Ölstugan tullen {}'.format(name1)
        f_name2 = 'Ölstugan tullen {}'.format(name2)
        res = gmaps.distance_matrix(
            f_name1, f_name2, mode=mode, departure_time=NOW)['rows'][0]['elements'][0]
        distance = int(res['distance']['value'])
        duration = int(res['duration']['value'])
        durations[names.index(name1)][names.index(name2)] = duration
        durations[names.index(name2)][names.index(name1)] = duration
        distances[names.index(name1)][names.index(name2)] = distance
        distances[names.index(name2)][names.index(name1)] = distance

        stdout.write('\rPairs handled: {}/{}'.format(i+1, len(pairs)))
        stdout.flush()

    return durations, distances
