# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:

def vragenlijst():
    # De vragen die je aan de feestgangers gaat stellen
    vragen = [
        "Wat is je voornaam?",
        "Wat is je achternaam?",
        "Wat neem je mee aan drank?",
        "Wat neem je mee om te eten?"
    ]
    
    # De lijst om de gegevens van de feestganger op te slaan
    feestganger = {}

    # Vraag de feestganger naar zijn/haar antwoorden
    print("Vragenlijst voor de party!")
    for i, vraag in enumerate(vragen, 1):
        antwoord = input(f"{i}. {vraag}\n")
        if i == 1:
            feestganger["voornaam"] = antwoord
        elif i == 2:
            feestganger["achternaam"] = antwoord
        elif i == 3:
            feestganger["drank"] = antwoord
        elif i == 4:
            feestganger["eten"] = antwoord
    
    # Bedank de feestganger voor het invullen
    print("\nBedankt voor het invullen!")
    print("See you at the party.\n")
    
    # Resultaten opslaan in een tekstbestand
    with open("feestganger_gegevens.txt", "a") as bestand:
        bestand.write("----\n")
        for key, value in feestganger.items():
            bestand.write(f"{key}: {value}\n")
        bestand.write("\n")

# Functie aanroepen
vragenlijst()