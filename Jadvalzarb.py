#Multiplication table
print( "                         welcome                      ")
print ( "                       by   jey                      ")
while True:
    jadvalzarb=int(input("Do U Want Make A Costomise ؟ Yes Type 1 And No Type 2: "))
    if jadvalzarb==1:
        
        n = int(input("Please Enter n: "))
        m = int(input("Please Enter m: "))

        # ساخت جدول ضرب
        for i in range(1, n+1):
            for j in range(1, m+1):
                print(i*j, end='\t')
            print()
    elif jadvalzarb==2:
        quit()
    else:
        print("Enter Choise Currect Number!!!! ")
