# Opdracht 1 functies
# Naam student:
# Groep:

# importeer de module csv...

import csv

def lees_csv(bestandspad):
    with open(bestandspad, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        return [rij for rij in reader]

def schrijf_csv(bestandspad, data):
    with open(bestandspad, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

        from 095_modules import csv

# Maak voorbeelddata
data = [
    ['Naam', 'Leeftijd'],
    ['Ali', '22'],
    ['Sophie', '19'],
    ['Daan', '25']
]

# Schrijf de data naar een CSV-bestand
csv.schrijf_csv('voorbeeld.csv', data)

# Lees de data weer in
gelezen_data = csv.lees_csv('voorbeeld.csv')
print("Ingelezen CSV data:")
for rij in gelezen_data:
    print(rij)