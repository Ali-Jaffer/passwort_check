import re

def pruefe_passwort(passwort):
    punkte = 0

    # Länge prüfen
    if len(passwort) >= 8:
        punkte += 1
    if len(passwort) >= 12:
        punkte += 1

    # Kleinbuchstaben
    if re.search(r"[a-z]", passwort):
        punkte += 1

    # Grossbuchstaben
    if re.search(r"[A-Z]", passwort):
        punkte += 1

    # Zahlen
    if re.search(r"\d", passwort):
        punkte += 1

    # Sonderzeichen
    if re.search(r"[^\w\s]", passwort):
        punkte += 1

    # Bewertung
    if punkte <= 3:
        return "Nicht sicher"
    elif punkte <= 5:
        return "Neutral"
    else:
        return "Sicher"


if __name__ == "__main__":
    pw = input("Bitte Passwort eingeben: ")
    print("Ergebnis:", pruefe_passwort(pw))
