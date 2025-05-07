# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random

prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)
pogingen = 0
geraden = False

while not geraden:
    gok = int(input(prompt))
    pogingen += 1

    if gok < geheim_getal:
        print("hoger")
    elif gok > geheim_getal:
        print("lager")
    else:
        print(f"Je hebt het getal geraden het is {geheim_getal}!")
        print(f"Je hebt het in {pogingen} keer gedaan")
        geraden = True