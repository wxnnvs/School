bedrag = int(input("aankoopbedrag?   "))
gewicht = int(input("gewicht?         "))

if gewicht>100:
    kost = 40
else:
    if bedrag<50:
        kost = 10
    elif bedrag<100:
        kost = 5
    else:
        kost = "free shipping"

print(kost)