import math
def calculateSistaSida(sida1, sida2, vinkel):
    a = math.pow(sida1, 2) + math.pow(sida2, 2)
    b = 2 * sida2 * sida1 * math.cos(math.radians(vinkel))
    return round(math.sqrt(a - b))

sida1 = float(input("Ange sida1: "))
sida2 = float(input("Ange sida2: "))
vinkel = float(input("Vinkeln mellan dessa sidor: "))
sida3 = calculateSistaSida(sida1,sida2,vinkel)
print(sida3)
if sida1 == sida2 and sida1 == sida3:
    print("Liksidig")
elif sida1 != sida2 and sida1 != sida3
us
