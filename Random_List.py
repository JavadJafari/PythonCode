
import random
myList=[]

while True:
        Access=int(input("Do u want Create a Random List? : 1=Yes , 2=No :"))
        if Access==1:
            Numberoflist=int(input("How Much Number u Want Be in List? :"))
            range1=int(input("Enter Fist Range :"))
            range2=int(input("Enter End Range : "))
            my_list = list(set(random.sample(range(range1, range2), Numberoflist)))

            print(my_list)
        else:
              break

        