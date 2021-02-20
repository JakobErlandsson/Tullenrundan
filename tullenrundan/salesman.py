import numpy as np
from sys import stdout
from itertools import permutations


def travelling_salesman(names, distances, durations):
    '''
    Arguments: 
        names:     List of the different pubs
        distances: Symmetric matrix of distances between pubs
        durations: Symmetric matrix of travel duration between pubs
    Returns: 
        - List of pub indices leading to los total duration.
        - The duration
        - The distance of the path with the lowest duration
    Complexity: O(n!) where n is length of n-1 :(
    '''
    # According to Adam Andersson, the rules say we have to finish
    # at Andra Lång. As such the element is removed and then
    # placed last in every permutation of the route to assure this.
    # Because lists are immutable and because permutations() produces
    # a list of tuples rather than lists we have to do some magic here.
    n_copy = names.copy()
    n_copy.remove("Andra Lång")
    perms = list(permutations(n_copy))
    perms = [x + ("Andra Lång",) for x in perms]
    best_time = np.infty
    # Only time gets compared so the "best" distance
    # will be that of the route with the shortest duration of travel
    best_distance = np.infty
    best_route = 0
    for (i, p) in enumerate(perms):
        time = 0
        distance = 0
        for j in range(len(p)-1):
            start_index = names.index(p[j])
            end_index = names.index(p[j+1])
            time += durations[start_index][end_index]
            distance += distances[start_index][end_index]
        if(time < best_time):
            best_time = time
            best_route = i
            best_distance = distance
        stdout.write('\rPermutaions handled: {}/{}'.format(i+1, len(perms)))
        stdout.flush()

    return perms[best_route], best_time, best_distance
