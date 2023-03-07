from extraction import content
import pandas as pd

pokemon_list = content()

df = pd.DataFrame.from_dict(pokemon_list)
df.index += 1
df.to_csv("planilha.csv", index_label = "id")
