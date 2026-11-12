import random

FARBEN = ["kreuz", "blatt", "herz", "karo"]
WERTE = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "D", "K", "A"]

# Farbe = karte // 13   (0 bis 3)
# Wert  = karte % 13    (0 bis 12)


def karte_als_text(karte):
    return WERTE[karte % 13] + "-" + FARBEN[karte // 13]


def hand_geben():
    hand = []
    while len(hand) < 5:
        karte = random.randint(0, 51)
        if karte not in hand:
            hand.append(karte)
    return hand


def hand_anzeigen(hand):
    print("Hand:")
    for karte in hand:
        print(karte_als_text(karte))
    print("Zahlen:", hand)


def kombination_finden(hand):
    # zählen wie oft jeder Wert vorkommt
    anzahl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for karte in hand:
        anzahl[karte % 13] = anzahl[karte % 13] + 1

    paare = 0
    drillinge = 0
    vierlinge = 0
    for a in anzahl:
        if a == 2:
            paare = paare + 1
        if a == 3:
            drillinge = drillinge + 1
        if a == 4:
            vierlinge = vierlinge + 1

    # Flush: alle Karten haben die gleiche Farbe wie die erste
    flush = True
    for karte in hand:
        if karte // 13 != hand[0] // 13:
            flush = False

    # Straße: Werte sortieren, jeder muss 1 größer sein als der davor
    werte = []
    for karte in hand:
        werte.append(karte % 13)
    werte.sort()

    straße = True
    for i in range(4):
        if werte[i + 1] != werte[i] + 1:
            straße = False
    if werte == [0, 1, 2, 3, 12]:   # Sonderfall A-2-3-4-5
        straße = True

    # von der besten zur schlechtesten Kombination prüfen
    if straße and flush and werte[0] == 8:
        return "Royal Flush"
    elif straße and flush:
        return "Straight Flush"
    elif vierlinge == 1:
        return "Vierling"
    elif drillinge == 1 and paare == 1:
        return "Full House"
    elif flush:
        return "Flush"
    elif straße:
        return "Straße"
    elif drillinge == 1:
        return "Drilling"
    elif paare == 2:
        return "Zwei Paare"
    elif paare == 1:
        return "Paar"
    else:
        return "Hohe Karte"


# ------------------------------------------------------------
# Hauptprogramm
# ------------------------------------------------------------

hand = hand_geben()
hand_anzeigen(hand)
print("Kombination:", kombination_finden(hand))
print()

SPIELE = 100000

namen = ["Royal Flush", "Straight Flush", "Vierling", "Full House", "Flush",
         "Straße", "Drilling", "Zwei Paare", "Paar", "Hohe Karte"]
zaehler = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# richtige Werte in Prozent
richtig = [0.000154, 0.00139, 0.0240, 0.1441, 0.1965,
           0.3925, 2.1128, 4.7539, 42.2569, 50.1177]

print("Spiele", SPIELE, "mal")

for spiel in range(SPIELE):
    ergebnis = kombination_finden(hand_geben())
    for i in range(len(namen)):
        if namen[i] == ergebnis:
            zaehler[i] = zaehler[i] + 1

print()
print("Kombination       Anzahl   Simuliert %   Richtig %   Unterschied")
print("-----------------------------------------------------------------")

for i in range(len(namen)):
    prozent = zaehler[i] / SPIELE * 100
    unterschied = prozent - richtig[i]
    print(namen[i], zaehler[i], round(prozent, 4), richtig[i], round(unterschied, 4))