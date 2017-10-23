"""Evaluate given coordinates and validate that they are valid lat and lon.

Best : daddepledge
    def is_valid_coordinates(coordinates):
    try:
        lat, lng = [abs(float(c)) for c in coordinates.split(',') if 'e'
        not in c]
    except ValueError:
        return False

    return lat <= 90 and lng <= 180

"""


def is_valid_coordinates(coordinates):
    """Use given coordinates to validate lat and lon."""
    import re
    regex = re.compile("/[^-, .\d]/g")
    try:
        if not (coordinates.count(' ') == 1):
            return False
        print('so far so good 1')
        num_coords = coordinates.split(', ')
        if num_coords[0].count('.') > 1 or num_coords[1].count('.') > 1:
            return False
        if (regex.search(coordinates)):
            return False
        for ch in coordinates:
            if ch.isalpha():
                return False
        print('so far so good 2')
        print (re.search(regex, coordinates))
        if -90 <= float(num_coords[0]) <= 90 and\
           -180 <= float(num_coords[1]) <= 180:

            print('so far so good 3')
        else:
            return False
    except:
        return False
    return True
