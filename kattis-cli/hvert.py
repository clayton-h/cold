################################################
# Filename: hvert.py                            #
# Author: Clayton Hodges                       #
# Date Created: October 10, 2023               #
# Last Updated: October 13, 2023               #
# Description: This is a code solution for     #
# the Kattis problem Hvert Skal Maeta.         #
################################################

# dictionary to store cities and their
# respective distances to Reykjavik and Akureyri
cities = {
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
    'Mulating': {'Reykjavik': 603, 'Akureyri': 216},
    'Seltjarnarnes': {'Reykjavik': 4, 'Akureyri': 390}
}


def findCloserCity(input_city, cities) -> str:
    closest_city = None

    for city in cities.items():
        # skip over the input city's own listing
        if city == input_city:
            continue

        # find the shorter distance between the two cities
        if cities[input_city]['Reykjavik'] > cities[input_city]['Akureyri']:
            closest_city = 'Akureyri'
        else:
            closest_city = 'Reykjavik'

    return closest_city


def readFile() -> str:
    # open the input file in read mode
    with open('1.in', 'r') as file:
        content = file.read().strip()
        return content
    # file automatically closes


def main() -> None:
    # read in the text file
    # find the closest city
    # print it out
    print(findCloserCity(readFile(), cities))

    print("exiting main...")


if __name__ == "__main__":
    main()
