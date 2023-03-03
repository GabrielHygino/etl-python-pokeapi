from requests import get
from json import loads
import pandas as pd

pokemon_list = []
response = get(f"https://pokeapi.co/api/v2/pokemon?limit=1200")
formated_response = loads(response._content.decode())

for pokemon in formated_response["results"]:
    pokemon_list.append(pokemon)

df = pd.DataFrame.from_dict(pokemon_list)
df.index += 1
df.to_csv("planilha.csv", index_label = "id")
