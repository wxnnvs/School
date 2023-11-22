from math import *

kleinste = float(input("kleinste zijde:    "))
middelste = float(input("middelste zijde:   "))
grootste = float(input("grootste zijde:    "))

if sqrt((kleinste**2)+(middelste**2))<grootste**2:
    print("Stompe driehoek")
elif sqrt((kleinste**2)+(middelste**2))>grootste**2:
    print("Scherpe driehoek")
else:
    print("Rechte driehoek")