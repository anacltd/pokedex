import re
import sqlite3
import sys

from PIL import Image
from fuzzywuzzy import fuzz
from unidecode import unidecode

print("Pokedex\nBienvenu jeune dresseur !\nRechercher un pokémon\n")
choice = input("<A> Recherche par nom\n<B> Recherche par ID\n(sélectionner A ou B)\n")
choice.upper()
while choice not in ["A", "B"]:
    choice = input("Veuillez sélectionner A ou B\n")

try:
    conn = sqlite3.connect('pokemons.db')
    crsr = conn.cursor()
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM pokemons;")
    schema = cur.fetchone()

    names = c.execute("SELECT Nom FROM pokemons;").fetchall()
    request = ""

    if choice == "A":
        npt = input("\nEntrer le nom du pokémon\n> ")
        npt = unidecode(npt.title().strip())
        if npt not in names:
            for n in names:
                if fuzz.ratio(npt, n) > 80:
                    request = f"SELECT * FROM pokemons WHERE Nom = '{n}';"
                    break
        else:
            request = f"SELECT * FROM pokemons WHERE Nom = '{npt}';"

    else:
        npt = input("\nEntrer l'ID du pokémon\n> ")
        while len(npt) != 3:
            npt = "0" + npt
        request = f"SELECT * FROM pokemons WHERE ID = '{npt}';"
    print("\n")
    try:
        data = crsr.execute(request).fetchall()
        if data:
            for field, d in zip(schema.keys(), data[0]):
                print(f"{field} : {d}")
            idx = re.sub(r"^0*", "", data[0][0])
            try:
                path = f'pokemon\\{idx}.png' if sys.platform == "win32" else f'pokemon/{idx}.png'
                im = Image.open(path)
                im.show()

            except FileNotFoundError as e:
                print(f"Une erreur s'est produite ({e})")

    except IndexError as ie:
        print(f"Une erreur s'est produite ({ie}).\nVeuillez réessayer")


except sqlite3.Error as error:
    print(f"Problème de connexion à la base de données ({error})")
