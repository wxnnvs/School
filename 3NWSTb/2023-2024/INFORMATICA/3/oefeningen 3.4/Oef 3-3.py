verbruik = float(input("Verbruik per 100 km = "))
prijs = float(input("Benzineprijs = "))

kmkost = verbruik*prijs/100

print("5 km = €",round(5*kmkost,2))
print("25 km = €",round(25*kmkost,2))
print("100 km = €",round(100*kmkost,2))

#ALTERNATIEF zonder tussenberekening
#print("5 km = €",round(verbruik*prijs/20,2)) 
#print("25 km = €",round(verbruik*prijs/4,2))
#print("100 km = €",round(verbruik*prijs,2))


