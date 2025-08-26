from math import pi, sqrt

def berechne_Am(RIL, GROSS, KLEIN, GT):
    teil_1 = (GROSS * GT + KLEIN * GT) / 2
    teil_2 = (GROSS * GT - KLEIN * GT) / (2 * pi)
    Am_quadrat = ((RIL - teil_1) / 2) ** 2 - teil_2 ** 2
    if Am_quadrat < 0:
        raise ValueError("Ungültige Eingaben: negativer Wert unter der Wurzel.")
    return sqrt(Am_quadrat)

def berechne_RIL(Am, GROSS, KLEIN, GT):
    teil_1 = 2 * sqrt(Am**2 + ((GROSS * GT - KLEIN * GT) / (2 * pi))**2)
    teil_2 = (GROSS * GT + KLEIN * GT) / 2
    return teil_1 + teil_2

def berechne_GT(RIL, GROSS, KLEIN, Am, schritte=1000):
    min_gt = 1.0   # kleinster sinnvoller Zahnabstand in mm
    max_gt = 50.0  # größter sinnvoller Zahnabstand in mm
    toleranz = 0.001

    def ril_aus_gt(GT):
        teil_1 = 2 * sqrt(Am**2 + (((GROSS * GT - KLEIN * GT) / (2 * pi))**2))
        teil_2 = (GROSS * GT + KLEIN * GT) / 2
        return teil_1 + teil_2

    for _ in range(schritte):
        mitte = (min_gt + max_gt) / 2
        berechneter_ril = ril_aus_gt(mitte)

        if abs(berechneter_ril - RIL) < toleranz:
            return mitte
        elif berechneter_ril < RIL:
            min_gt = mitte
        else:
            max_gt = mitte

    return mitte

def berechne_GROSS(RIL, KLEIN, GT, Am, schritte=1000):
    # Numerische Näherung per binärer Suche
    min_gross = KLEIN + 1
    max_gross = 500  # beliebiges sinnvolles Limit
    toleranz = 0.01

    def ril_aus_gross(GROSS):
        teil_1 = 2 * sqrt(Am**2 + (((GROSS * GT - KLEIN * GT) / (2 * pi))**2))
        teil_2 = (GROSS * GT + KLEIN * GT) / 2
        return teil_1 + teil_2

    for _ in range(schritte):
        mitte = (min_gross + max_gross) / 2
        berechneter_ril = ril_aus_gross(mitte)

        if abs(berechneter_ril - RIL) < toleranz:
            return mitte
        elif berechneter_ril < RIL:
            min_gross = mitte
        else:
            max_gross = mitte

    return mitte  # Rückgabe des letzten Wertes (näherungsweise)

def berechne_KLEIN(RIL, GROSS, GT, Am, schritte=1000):
    min_klein = 1
    max_klein = GROSS - 1  # logisch kleiner als GROSS
    toleranz = 0.01

    def ril_aus_klein(KLEIN):
        teil_1 = 2 * sqrt(Am**2 + (((GROSS * GT - KLEIN * GT) / (2 * pi))**2))
        teil_2 = (GROSS * GT + KLEIN * GT) / 2
        return teil_1 + teil_2

    for _ in range(schritte):
        mitte = (min_klein + max_klein) / 2
        berechneter_ril = ril_aus_klein(mitte)

        if abs(berechneter_ril - RIL) < toleranz:
            return mitte
        elif berechneter_ril < RIL:
            min_klein = mitte
        else:
            max_klein = mitte

    return mitte

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Bitte eine ganze Zahl eingeben.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Bitte eine Zahl eingeben (Kommazahl erlaubt).")

def hauptmenue():
    print("Was möchtest du berechnen?")
    print("1 - Großes Ritzel (GROSS)")
    print("2 - Kleines Ritzel (KLEIN)")
    print("3 - Zahnabstand GT")
    print("4 - Riemenlänge (RIL)")
    print("5 - Achsabstand (Am)")
    
    while True:
        wahl = input("Deine Auswahl (1-5): ")
        if wahl in ["1", "2", "3", "4", "5"]:
            return int(wahl)
        print("Ungültige Auswahl. Bitte 1 bis 5 eingeben.")

def main():
    print("Berechnungstool für Riemenantrieb\n")
    auswahl = hauptmenue()

    try:
        if auswahl == 1:
            # GROSS berechnen – nicht unterstützt
            print("\nBerechnung des großen Ritzels (GROSS)")
            RIL = get_float_input("Riemenlänge RIL (in mm): ")
            KLEIN = get_int_input("Anzahl Zähne kleines Ritzel: ")
            GT = get_float_input("Zahnabstand GT (in mm): ")
            Am = get_float_input("Achsabstand Am (in mm): ")

            GROSS = berechne_GROSS(RIL, KLEIN, GT, Am)
            print(f"\nGroßes Ritzel GROSS ≈ {round(GROSS)} Zähne")

        elif auswahl == 2:
            print("\nBerechnung des kleinen Ritzels (KLEIN)")
            RIL = get_float_input("Riemenlänge RIL (in mm): ")
            GROSS = get_int_input("Anzahl Zähne großes Ritzel: ")
            GT = get_float_input("Zahnabstand GT (in mm): ")
            Am = get_float_input("Achsabstand Am (in mm): ")

            KLEIN = berechne_KLEIN(RIL, GROSS, GT, Am)
            print(f"\nKleines Ritzel KLEIN ≈ {round(KLEIN)} Zähne")

        elif auswahl == 3:
            print("\nBerechnung des Zahnabstands GT")
            RIL = get_float_input("Riemenlänge RIL (in mm): ")
            GROSS = get_int_input("Anzahl Zähne großes Ritzel: ")
            KLEIN = get_int_input("Anzahl Zähne kleines Ritzel: ")
            Am = get_float_input("Achsabstand Am (in mm): ")

            GT = berechne_GT(RIL, GROSS, KLEIN, Am)
            print(f"\nZahnabstand GT ≈ {round(GT, 3)} mm")

        elif auswahl == 4:
            # RIL berechnen
            print("\nBerechnung der Riemenlänge (RIL)")
            Am = get_float_input("Achsabstand Am (in mm): ")
            GROSS = get_int_input("Anzahl Zähne großes Ritzel: ")
            KLEIN = get_int_input("Anzahl Zähne kleines Ritzel: ")
            GT = get_float_input("Zahnabstand GT (in mm): ")

            RIL = berechne_RIL(Am, GROSS, KLEIN, GT)
            print(f"\nRiemenlänge RIL = {round(RIL, 2)} mm")

        elif auswahl == 5:
            # Am berechnen
            print("\nBerechnung des Achsabstands (Am)")
            RIL = get_float_input("Riemenlänge RIL (in mm): ")
            GROSS = get_int_input("Anzahl Zähne großes Ritzel: ")
            KLEIN = get_int_input("Anzahl Zähne kleines Ritzel: ")
            GT = get_float_input("Zahnabstand GT (in mm): ")

            Am = berechne_Am(RIL, GROSS, KLEIN, GT)
            print(f"\nAchsabstand Am = {round(Am, 2)} mm")

    except ValueError as e:
        print("\nFEHLER:", e)

    except NotImplementedError as e:
        print("\nNoch nicht verfügbar:", e)

if __name__ == "__main__":
    main()

