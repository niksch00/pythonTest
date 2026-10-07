# Notenrechner: liest Noten ein und berechnet Durchschnitt, beste und schlechteste Note.

BESTE_NOTE = 1.0
SCHLECHTESTE_NOTE = 6.0
BESTANDEN_BIS = 4.0


def noten_einlesen():
    """Fragt so lange nach Noten, bis eine gültige Eingabe gemacht wurde."""
    while True:
        eingabe = input("Noten kommagetrennt eingeben (z.B. 1.3, 2.7, 3.0): ")
        teile = eingabe.split(",")

        noten = []
        fehler = False

        for teil in teile:
            teil = teil.strip()

            if teil == "":
                print("Fehler: Leere Note gefunden. Bitte erneut versuchen.")
                fehler = True
                break

            try:
                note = float(teil)
            except ValueError:
                print(f"Fehler: '{teil}' ist keine gültige Zahl. Bitte erneut versuchen.")
                fehler = True
                break

            if note < BESTE_NOTE or note > SCHLECHTESTE_NOTE:
                print(f"Fehler: {teil} liegt nicht zwischen {BESTE_NOTE} und {SCHLECHTESTE_NOTE}.")
                fehler = True
                break

            noten.append(note)

        if not fehler:
            return noten


def formatieren(zahl):
    """Gibt eine Zahl mit zwei Nachkommastellen und deutschem Komma aus."""
    return f"{zahl:.2f}".replace(".", ",")


def main():
    noten = noten_einlesen()

    durchschnitt = sum(noten) / len(noten)
    beste = min(noten)  # kleinere Note = bessere Note
    schlechteste = max(noten)

    print(f"Durchschnitt:       {formatieren(durchschnitt)}")
    print(f"Beste Note:         {formatieren(beste)}")
    print(f"Schlechteste Note:  {formatieren(schlechteste)}")

    if durchschnitt <= BESTANDEN_BIS:
        print("Ergebnis: bestanden")
    else:
        print("Ergebnis: nicht bestanden")


if __name__ == "__main__":
    main()
