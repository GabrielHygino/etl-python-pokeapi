from extraction import content
from pymongo import MongoClient

pokemon_list = content()
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["pokemon"]
collections = mydb["pokedex"]
collections.insert_many(pokemon_list)
