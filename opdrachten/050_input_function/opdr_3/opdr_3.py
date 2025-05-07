# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

input_string = input("Voer minimaal 5 objecten in, gescheiden door een komma: ")

objecten_lijst = [item.strip() for item in input_string.split(",")]

objecten_lijst.sort(reverse=True)

print(objecten_lijst)