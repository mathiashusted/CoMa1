MANTISSE = 3

""""
a) Schreiben Sie eine Funktion runden(x, L), die eine Eingabezahl x auf L Stellen
rundet.
Zur Klarstellung: Dies soll gerade der Abbildung rd nach G(10, L) aus der Vorle-
sung mit kaufmännischem Runden entsprechen, also insbesondere nicht der Dar-
stellung als Festkommazahl.

"""

def runden(x, L):
    exp = 0
    neg = False
    if x < 0:
        neg = True
        x = abs(x)
    
    while (x//1 != 0):
        exp += 1
        x /= 10
    
    x_as_string = str(x)
    x_mantissa = x_as_string[0:L+2]
    x_mantissa = float(x_mantissa)

    if L+2 < len(x_as_string) and int(x_as_string[L+2]) >= 5:
        x_mantissa = x_mantissa + pow(10, -L)

    # Hier muss eine Rundung angewendet werden, da Python sonst bei bestimmten Zahlen
    # eine lange Nachkommastelle bildet, ironischerweise genau wegen der Rundungsmechanismen,
    # die diese Funktion implementiert.😂 Es macht jedoch keinen Unterschied in der Funktionalität
    if neg == False:
        return round(x_mantissa*pow(10,exp), L)
    else:
        return -round(x_mantissa*pow(10,exp), L)



"""
b) Schreiben Sie Funktionen add(x, y, rd) und mult(x, y, rd). Hierbei sind x
und y skalare Zahlen und rd ist eine Rundungsfunktion (wie beispielsweise runden(·,L)
aus der vorangegangenen Unteraufgabe für festes L). Als Rückgabewert wird die
mit rd gerundete Summe bzw. Produkt der ebenfalls mit rd gerundeten Skalare x
und y erwartet.
"""


# Es wurde exemplarisch die Mantisse, die als Konstante definiert wurde, gewählt
def add(x, y, rd):
    x = rd(x, MANTISSE)
    y = rd(y, MANTISSE)
    return rd((x+y), MANTISSE)

def mult(x, y, rd):
    x = rd(x, MANTISSE)
    y = rd(y, MANTISSE)
    return rd((x*y), MANTISSE)


"""
c) Schreiben Sie eine Funktion c = binomA(a, b, rd), die die erste binomische For-
mel nach der Vorschrift
(~a + ~b)^(2)
auswertet und in der Variablen c zurückgibt, wobei ~a und ~b die mit rd gerundeten
Werte von a und b sind und wobei die Ergebnisse von Addition und Multiplikation
ebenso mit rd gerundet werden. Nutzen Sie hierfür die Funktionen add und mult
aus der vorangegangenen Unteraufgabe.
"""

def binomA(a, b, rd):
    aa = rd(a, MANTISSE)
    bb = rd(b, MANTISSE)
    bin = pow(add(aa, bb, rd), 2)
    return bin

"""
d) Schreiben Sie analog zur vorangegangenen Unteraufgabe eine Funktion c = binomB(a, b, rd), 
die nun jedoch die erste binomische Formel nach der Vorschrift
~a2 + 2~a~b + ~b2
auswertet
"""

def binomB(a, b, rd):
    aa = rd(a, MANTISSE)
    bb = rd(b, MANTISSE)
    bin = pow(aa, 2) + (2*aa*bb) + pow(bb,2)
    return bin


"""
e) Nutzen Sie Ihre Funktionen binomA und binomB mit rd = runden(·,L), um für a =
0,012345 und b = −0,01234 zu entscheiden, welche der beiden Darstellungen der
binomischen Formel in diesem Fall die bessere ist. Betrachten Sie dabei verschiede-
ne Werte für L und versuchen Sie das beobachtete Verhalten zu erklären. Schreiben
Sie Ihre Antwort in eine Text-Datei mit dem Namen beobachtungen.txt.
Hinweis: Sie sollten Ihre Argumentation auf konkrete Daten stützen, die Sie eben-
so in die Text-Datei aufnehmen."""

c = binomA(273,526, runden)
print(c)

a = 0.012345
b = -0.01234

calcBin = a*a + 2*a*b + b*b # Referenzwert für das Binom

calcBinA = binomA(a,b, runden)
calcBinB = binomB(a,b, runden)

if (abs(calcBin - calcBinA)) < (abs(calcBin - calcBinB)):
    print("binomA ist besser")
else:
    print("binomB ist besser")

"""
f) (2 TP Bonuspunkte)
Vergleichen Sie die Ausgabe der folgenden Ausdr¨ucke in Python:
 print(0.1)
 print(0.1*10 + 0.1*(-9))
 print(add(mult(0.1,10, rd), mult(0.1,-9, rd), rd))
Hierbei soll rd das Runden in G(10, 5) mittels runden(·, 5) bezeichnen.
Welches Resultat erwarten Sie? Wie lassen sich die unterschiedlichen Ergebnisse
erkl¨aren?
"""

print(0.1) # => 0.1
print(0.1*10 + 0.1*(-9)) # => 0.09999999999999998
print(add(mult(0.1,10, runden), mult(0.1,-9, runden), runden)) # => 0.1
"""
Antwort:
0.1 ist trivial, da eine Nachkommastelle leicht dargestellt werden kann.

(0.1*10 + 0.1*(-9)), anders ausgedrückt 1-0.9, ergibt 0.09999999999999998.
In Binär ist 0.9 kein endlicher Bruch. Dementsprechend ist ein gewisser Fehler bei der diskreten Berechnung damit unmöglich auszuschließen.
Verwenden wir unsere add() Funktion auf die gerundeten Zahlen, so wird nach dem Aufaddieren die runden() Funktion angewendet.
"""

# Test
print(runden(28226.5,5))