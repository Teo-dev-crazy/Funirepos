# Opdracht 1 while-loops
# Naam student:
# Groep:

vraag1 = input("Wat vind je van de huidige regering?\n")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe?\n")
vraag3 = input("Wat vind jij de mooiste stad van Nederland?\n")

with open("enquete_resultaten.txt", "w") as bestand:
    bestand.write("Enquête Resultaten:\n")
    bestand.write(f"1. Huidige regering: {vraag1}\n")
    bestand.write(f"2. Python-lessen: {vraag2}\n")
    bestand.write(f"3. Mooiste stad: {vraag3}\n")

print("Bedankt voor het invullen! Je antwoorden zijn opgeslagen.")