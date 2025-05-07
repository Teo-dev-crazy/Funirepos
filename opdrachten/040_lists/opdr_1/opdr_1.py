# Opdracht 1 lists
# Naam student:
# Groep

lijst = []

persoon1 = {"id": 0, "voornaam": "Emma", "achternaam": "Jansen"}
persoon2 = {"id": 1, "voornaam": "Noah", "achternaam": "De Vries"}
persoon3 = {"id": 2, "voornaam": "Sophie", "achternaam": "Bakker"}
persoon4 = {"id": 3, "voornaam": "Liam", "achternaam": "Peters"}

lijst.extend([persoon1, persoon2, persoon3, persoon4])

print(lijst[1]["voornaam"], lijst[1]["achternaam"])