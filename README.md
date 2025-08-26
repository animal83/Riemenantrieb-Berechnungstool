# Riemenantrieb Berechnungstool

Dieses Python-Skript ist ein interaktives Tool zur Berechnung verschiedener Kenngrößen eines Riemenantriebs, wie z. B.:

- Achsabstand (Am)
- Riemenlänge (RIL)
- Zahnabstand (GT)
- Anzahl Zähne des großen Ritzels (GROSS)
- Anzahl Zähne des kleinen Ritzels (KLEIN)

## 📐 Anwendungsbereiche

Das Tool kann z. B. beim Entwurf oder der Analyse von Zahnriemenantrieben verwendet werden, insbesondere bei der Umrechnung und Optimierung von Riemenlänge und Achsabständen in Abhängigkeit von Zahnradgrößen und Zahnabstand.

## ▶️ Nutzung

### Start

Das Programm wird über die Konsole gestartet:

```bash
python main.py

Interaktive Auswahl

Nach dem Start fragt das Tool:

Was möchtest du berechnen?
1 - Großes Ritzel (GROSS)
2 - Kleines Ritzel (KLEIN)
3 - Zahnabstand GT
4 - Riemenlänge (RIL)
5 - Achsabstand (Am)

```

Je nach Auswahl wirst du zur Eingabe der erforderlichen Werte (z. B. Riemenlänge, Zahnanzahl, etc.) aufgefordert. Anschließend wird die gewünschte Größe berechnet und ausgegeben.

🔢 Beispiel

Angenommen, du möchtest den Achsabstand berechnen:

```bash

Wähle im Menü die Option 5 (Achsabstand).

Gib die folgenden Werte ein:

Riemenlänge RIL (in mm): 800
Anzahl Zähne großes Ritzel: 40
Anzahl Zähne kleines Ritzel: 20
Zahnabstand GT (in mm): 5


Ausgabe:

Achsabstand Am = 120.45 mm
```

⚙️ Implementierte Funktionen
Rechenfunktionen:

berechne_Am(RIL, GROSS, KLEIN, GT)

berechne_RIL(Am, GROSS, KLEIN, GT)

berechne_GT(RIL, GROSS, KLEIN, Am)

berechne_GROSS(RIL, KLEIN, GT, Am)

berechne_KLEIN(RIL, GROSS, GT, Am)

Für unbekannte Werte wird eine numerische Näherung per binärer Suche durchgeführt.

⚠️ Fehlerbehandlung

Bei ungültigen Eingaben (z. B. wenn eine Wurzel aus einem negativen Wert gezogen werden müsste) gibt das Programm eine entsprechende Fehlermeldung aus.

Eingaben werden überprüft (nur Zahlen erlaubt).

🧮 Mathematischer Hintergrund

Die Berechnungen basieren auf Formeln zur geometrischen Bestimmung der Riemenlänge eines Zahnriemenantriebs unter Berücksichtigung von:

Umfang des großen und kleinen Ritzels (Zähne × Zahnabstand)

Achsabstand zwischen den beiden Ritzeln

Korrekturen auf Basis der Geometrie (z. B. Bögen des Riemens um die Ritzel)

📄 Lizenz

Dieses Tool steht unter keiner speziellen Lizenz. Freie Nutzung und Modifikation für private oder berufliche Zwecke ist erlaubt.

