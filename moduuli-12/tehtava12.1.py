from collections import namedtuple

import requests
import json

start = input("Paina Enter, jos haluat Chuck Norris vitsin!")

pyyntö = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print("Tässä vitsisi!")
        print(json_vastaus["value"])

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")