# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def encryptie(tekst):
    encrypted_text = ""
    for char in tekst:
        if char.isalpha():  # Alleen letters encrypten
            # Verschillen van 'a' of 'A' om onderscheid te maken tussen kleine en hoofdletters
            base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr(base + (ord(char.lower()) - base + 5) % 26)
            # Zorg ervoor dat het dezelfde lettercase behoudt
            encrypted_text += encrypted_char if char.islower() else encrypted_char.upper()
        else:
            encrypted_text += char  # Andere tekens blijven ongewijzigd
    return encrypted_text

# Invoer
tekst = input("Geef de tekst die wilt encrypten..\n")

# Encryptie uitvoeren
encrypted = encryptie(tekst)

# Resultaat tonen
print(encrypted)

