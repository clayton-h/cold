################################################
# Filename: hvert.py                            #
# Author: Clayton Hodges                       #
# Date Created: October 10, 2023               #
# Last Updated: October 13, 2023               #
# Description: This is a code solution for     #
# the Kattis problem Hvert Skal Maeta.         #
################################################
from typing import Dict

# nested dictionaries to store cities and their
# respective distances to Reykjavik and Akureyri
global_cities = {
    'Reykjavik': {'Reykjavik': 0, 'Akureyri': 388},
    'Akureyri': {'Reykjavik': 388, 'Akureyri': 0},
    'Kopavogur': {'Reykjavik': 6, 'Akureyri': 387},
    'Hafnarfjordur': {'Reykjavik': 12, 'Akureyri': 391},
    'Reykjanesbaer': {'Reykjavik': 48, 'Akureyri': 427},
    'Gardabaer': {'Reykjavik': 9, 'Akureyri': 389},
    'Mosfellsbaer': {'Reykjavik': 16, 'Akureyri': 371},
    'Arborg': {'Reykjavik': 64, 'Akureyri': 428},
    'Akranes': {'Reykjavik': 49, 'Akureyri': 350},
    'Fjardabyggd': {'Reykjavik': 659, 'Akureyri': 290},
    'Mulathing': {'Reykjavik': 603, 'Akureyri': 216},
    'Seltjarnarnes': {'Reykjavik': 4, 'Akureyri': 390}
}


def find_closer_city(input_city: str, local_cities: Dict[str, Dict[str, int]]) -> str:
    """
    A function that finds and returns
    the closer of two cities given
    user input (city).

    Args:
        input_city (string): A city from user input.
        cities (dictionary): A dictionary containing cities
                             and their distances to two fixed
                             cities.

    Returns:
        str: The closest city.
    """
    closest_city = None

    # skip over the input city's own listing
    if input_city not in local_cities:
        return "1"

    # find the shorter distance between the two cities
    if local_cities[input_city]['Reykjavik'] > local_cities[input_city]['Akureyri']:
        closest_city = 'Akureyri'
    else:
        closest_city = 'Reykjavik'

    return closest_city


def main() -> None:
    """
    The main function takes user input (city),
    finds the closest city,
    and prints it out.
    """

    print(find_closer_city(input(), global_cities))


if __name__ == "__main__":
    main()
