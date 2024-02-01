kolommen = 0
kolommen_origineel = 0
dollar_teken = ""
max_dollars = 0
gebruikt = 0

max_dollars = int(input("Na hoeveel $-tekens moet ik stoppen?   "))
while max_dollars > 0:
    dollars = 0
    kolommen = int(input("Aantal kolommen?   "))
    kolommen_origineel = kolommen
    
    for x in range(kolommen_origineel):
        dollar_teken = ""
        for y in range(x+1):
            dollar_teken += "$ "
            dollars = dollars + 1
        print(dollar_teken)
    
    for x in range(kolommen_origineel):
        dollar_teken = ""
        for y in range(kolommen_origineel - x - 1):
            dollar_teken += "$ "
            dollars = dollars + 1
        print(dollar_teken)
    gebruikt += dollars
    max_dollars -= dollars
print("er zijn ", gebruikt, " gebruikt")