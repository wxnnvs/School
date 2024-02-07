bedrag = str(input("aankoopbedrag?   "))

if bedrag<50:
    print("kost: €10")
elif bedrag<100:
    print("kost: €5")
else:
    print("free shipping")