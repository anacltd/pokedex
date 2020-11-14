import sys

import pandas as pd
from PIL import Image
from fuzzywuzzy import fuzz
from unidecode import unidecode

data = pd.read_csv('dataset.csv', sep=";")

print("Pokedex\nBienvenu jeune dresseur !\nRechercher un pokémon\n")
choice = input("<A> Recherche par nom\n<B> Recherche par ID\n(sélectionner A ou B)\n")
choice.upper()
while choice not in ["A", "B"]:
    choice = input("Veuillez sélectionner A ou B\n")

if choice == "A":
    npt = input("\nEntrer le nom du pokémon\n> ")
    npt = unidecode(npt.title().strip())
    df = data[data['Nom'] == npt]

else:
    npt = input("\nEntrer l'ID du pokémon\n> ")
    df = data[data['ID'] == npt]

if len(df) == 0:
    for n in data['Nom'].values:
        if fuzz.ratio(npt, n) > 80:
            df = data[data['Nom'] == n]
            break

print("\n")
try:
    for (col_name, col_data) in df.iteritems():
        print(f"{col_name}: {col_data.values[0]}")
    idx = df.iloc[0]['ID']
    try:
        path = f'pokemon\\{idx}.png' if sys.platform == "win32" else f'pokemon/{idx}.png'
        im = Image.open(path)
        im.show()
    except FileNotFoundError as e:
        print(f"Une erreur s'est produite ({e})")
except IndexError as ie:
    print(f"Une erreur s'est produite ({ie}).\nVeuillez réessayer")
