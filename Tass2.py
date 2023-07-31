print("Wellcome To Tass Game Very Exciting Game Independed To Your Chance :) ")
print("Rules : if u bring 6 u can roll again just this :) ")
while True:
    total_toss=0
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
            Chance1=rn.randint(1,6)
            Chance2=rn.randint(1,6)
            print("Cong Your First Chance is " , Chance1 , " And Your Secoud Chance is" , Chance2)
            break