#Chess_Bord
print("                           Welcome                     ")
print("                         Chess Bord                     ")
print("                           By Jey                      ")

while True:
    Chess_bord=int(input("Start == 1 ,  Exit == 2 :"))
    if Chess_bord==1:
        row=int(input("Please Enter a number for row :"))
        col=int(input("Please Enter a number for col :"))
        def chess():
            for i in range(row):
                for j in range(col):
                    if (i+j) %2==0:            
                        print("#" , end=" ")
                    else:
                        print("*" , end=" ")
                print()
    if Chess_bord==2:
        break

    chess()