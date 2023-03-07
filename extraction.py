from requests import get
from json import loads

def content():

    pokemon_list = []
    response = get(f"https://pokeapi.co/api/v2/pokemon?limit=1500")
    formated_response = loads(response._content.decode())

    for pokemon in formated_response["results"]:
        pokemon_list.append(pokemon)
    return pokemon_list