print("Wellcome To Tass Game Very Exciting Game Independed To Your Chance :) ")
print("Rules : if u bring 6 u can roll again just this :) ")
while True:
    
    import random as rn
    Tass=str(input("Tasss Bendaz :)) >> Type 'Roll' "))
    if Tass=="Roll":
        tass= rn.randint(1,6)
        print(tass)
        if tass==1:
            result=1
            break
        if tass==2:
            result=2
            break
        if tass==3:
            result=3
            break
        if tass==4:
            result=4
            break
        if tass==5:
            result=5
            break
        if tass==6:
            result="6 // Tabrik Dobare Tass Bendaz"
            print(result)