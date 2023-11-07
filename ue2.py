#In dieser Aufgabe sollen Sie in Python eine Funktion implementieren, die ganze Zahlen
#im Dezimalsystem als Zahlen im Dualsystem darstellt. Gehen Sie dabei in mehreren
#Schritten vor:
#mplementieren Sie eine Funktion ntobasetwo(n, c), die eine natürliche Zahl
#n ∈ N in eine Binärzahl der Länge c umwandelt.

def ntobasetwo(n,c):
    output = []
    current = n
    for i in range(c):
        output.insert(0, current % 2 == True)
        current = current // 2
    return output

#Implementieren Sie eine Funktion complement(b), die das Zweierkomplement ei-
#ner Binärzahl entsprechend der Vorlesung berechnet. Dabei wird als Eingabe ein
#Vektor b erwartet mit bi ∈ {0, 1}. Der Rückgabewert soll auch ein Vektor ˆb mit
#ˆbi ∈ {0, 1} sein, sodass b und ˆb dieselbe Länge haben.

def complement(b):
    # b is vector
    for i in range(len(b)-1,-1,-1):
        if b[i] == True:
            b[i] = False
            break
        b[i] = True
    for i in range(len(b)):
        if b[i] == True:
            b[i] = False
        else:
            b[i] = True
    return b

#Implementieren Sie eine Funktion ztobasetwo(z, c), die eine ganze Zahl z ∈ Z
#in eine Binärzahl der Länge c umwandelt, wobei negative Zahlen mit Hilfe des
#Zweierkomplements realisiert werden. Verwenden Sie dabei die Funktionen aus
#den vorangegangenen Teilaufgaben

def ztobasetwo(z,c):
    if z > 0:
        return ntobasetwo(z,c)
    else:
        return complement(ntobasetwo(z,c))
