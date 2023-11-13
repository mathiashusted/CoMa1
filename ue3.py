MANTISSE = 3

""""
a) Schreiben Sie eine Funktion runden(x, L), die eine Eingabezahl x auf L Stellen
rundet.
Zur Klarstellung: Dies soll gerade der Abbildung rd nach G(10, L) aus der Vorle-
sung mit kaufmännischem Runden entsprechen, also insbesondere nicht der Dar-
stellung als Festkommazahl.

"""

def runden(x, L):
    neg = False
    y = str(x)
    num = []
    y = y.split(".")
    if y[0][0] == "-":
        neg = True
        cc = y[0].split("-")
        y[0] = cc[1]
    dec = len(y[0]) # Suche Stelle, wo Komma vorkommt
    y = ''.join(y)

    output = 0
    for i in range(0, len(y)):
        num.append(int(y[i]))

    for i in range(0, dec):
        output += num[i] *  pow(10, (dec-i-1))

    for i in range(dec, dec + L, 1):
        if i > len(num)-1:
            break
        output += num[i] * pow(10, -i-1+dec)

    if dec+L < len(y) and num[dec+L] >= 5:
        output += pow(10, -L)

    # Hier muss eine Rundung angewendet werden, da Python sonst bei bestimmten Zahlen
    # eine lange Nachkommastelle bildet, ironischerweise genau wegen der Rundungsmechanismen,
    # die diese Funktion implementiert.😂 Es macht jedoch keinen Unterschied in der Funktionalität

    if neg:
        return -round(output, L)
    else:
        return round(output, L)

"""
b) Schreiben Sie Funktionen add(x, y, rd) und mult(x, y, rd). Hierbei sind x
und y skalare Zahlen und rd ist eine Rundungsfunktion (wie beispielsweise runden(·,L)
aus der vorangegangenen Unteraufgabe für festes L). Als Rückgabewert wird die
mit rd gerundete Summe bzw. Produkt der ebenfalls mit rd gerundeten Skalare x
und y erwartet.
"""


# Es wurde exemplarisch 5 gewählt
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

if calcBinA < calcBinB:
    print("binomA ist schneller")
else:
    print("binomB ist schneller")

print(runden(286,2))