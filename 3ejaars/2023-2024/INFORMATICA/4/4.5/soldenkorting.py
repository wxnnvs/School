stuks = float(input("aantal stuks?   "))

if stuks==1:
    print("10%")
elif stuks==2 or stuks==3:
    print("20%")
elif stuks==4:
    print("30%")
elif stuks<=5:
    if float(input("hoeveel euro kostte dit?  "))<=300:
        print("50%")
    else:
        print("40%")