# Opdracht 2 berekeningen
# Naam student:
# Groep:


gasten = ["Paul", "Kees", "Marie", "Hilda"]
gasten.insert(0, "Teo") 
print(gasten)

gasten.remove("Marie")
print(gasten)

kees_index = gasten.index("Kees") 
gasten.insert(kees_index + 1, "George") 
print(gasten)

['Jij', 'Paul', 'Kees', 'Marie', 'Hilda']
['Jij', 'Paul', 'Kees', 'Hilda']
['Jij', 'Paul', 'Kees', 'George', 'Hilda']