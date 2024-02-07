som = 0

for x in range(1, 11):
    getal = float(input(f"hoeveel is getal {x}? "))
    som += getal

gemiddelde = som/10
print(f"Het gemiddelde van de getallen is {gemiddelde}")