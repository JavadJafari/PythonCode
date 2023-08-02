#Guess_Numbers
print("Wellcome To Guess Number Game , I Hope U enjoy it")
print("Created by 'Jey' ")
import random
pc_number=random.randint(1,5)
count=1
for i in range(10):
    user_number=int(input("Pls Enter Num Between 1 and 5 :"))
    if user_number==pc_number:
        print("u Win")
        print(" You Win With" , count , " Guesses")
        break
        
    if user_number<pc_number:
        print("Upper!")
    if user_number>pc_number:
        print("Downner")
    if user_number>5:
        print("Out Of Guess Range")
    count+=1  
