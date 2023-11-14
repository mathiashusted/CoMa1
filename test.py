def runden(x, L):
    exp = 0
    while (x//1 != 0):
        exp += 1
        x /= 10
    x_as_string = str(x)
    x_mantissa = x_as_string[0:L+2]
    x_mantissa = float(x_mantissa)

    if L+2 < len(x_as_string) and int(x_as_string[L+2]) >= 5:
        x_mantissa = x_mantissa + pow(10, -L)

    return round(x_mantissa*pow(10,exp), L)

print(runden(28226,4))