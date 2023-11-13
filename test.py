def runden(x, L):
    y = str(x)
    print("Input: " + y)
    num = []

    y = y.split(".")

    dec = len(y[0])
    y = ''.join(y)
    print("Dec at: " + str(dec) + "\nJoined number: " + str(y))

    output = 0
    for i in range(0, len(y)):
        num.append(int(y[i]))





    for i in range(0, dec):
        output += num[i] *  pow(10, (dec-i-1))




    for i in range(dec, dec + L, 1):
        if i > len(num)-1:
            break
        output += num[i] * pow(10, -i-1+dec)

    if dec+L < len(y) and num[dec+L] >= 5: # Achtung: num[L] entspricht hier a_(l+1)
        output += pow(10, -L)

    # Hier muss eine Rundung angewendet werden, da Python sonst bei bestimmten Zahlen
    # eine lange Nachkommastelle bildet, ironischerweise genau wegen der Rundungsmechanismen,
    # die diese Funktion implementiert.😂 Es macht jedoch keinen Unterschied in der Funktionalität

    return round(output, L)

print("Output: " + str(runden(145132.324,1)))