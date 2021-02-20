import argparse
from salesman import travelling_salesman
from maps_API import API_request

PARSER = argparse.ArgumentParser(description="Tullenrundan Göteborg")

# Skipping Mölndal to make it strictly Gothenburg and within the 'voi-zone'
NAMES = ['Kville', 'Majorna', 'Johanneberg', 'Wärdshuset',
         'Kålltorp', 'Lejonet', 'Andra Lång']


def __main__():
    PARSER.add_argument('-m', '--mode', dest='mode', default='bicycling',
                        help='Mode of transportation, one of:\n\tbicycling(default)\n\tdriving\n\twalking\n\ttransit')
    PARSER.add_argument('-k', '--key', dest='key', type=str,
                        help='API key for Google Maps')
    args = PARSER.parse_args()
    if not args.key:
        print("Please provide valid API key")
        return
    print('Fetching information about travel times...')
    durations, distances = API_request(args.mode, NAMES, args.key)
    # Start with newline because overwriting print does not produce new line
    print('\nDone fetching\n')

    route, time, distance = travelling_salesman(NAMES, distances, durations)

    print('\nBest route:\n\t{}\nRequires {} km of travel taking {} minutes.'.format(
        ' -> '.join(route), distance // 1000, time // 60))


__main__()
