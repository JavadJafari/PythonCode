#Creat Random List
print("                                          Wellcome                                       ")
print(" Create A Random List With Random Numbers")
print(" Created By 'Jey' ")
import random
myList=[]

while True:
        Access=int(input("Do u want Create a Random List? : 1=Yes , 2=No :"))
        if Access==1:
            Numberoflist=int(input("How Much Number u Want Be in List? :"))
            range1=int(input("Enter Fist Range :"))
            range2=int(input("Enter End Range : "))
            my_list = list(random.sample(range(range1, range2), Numberoflist))

            print(my_list)
        if Access==2:
              break

        