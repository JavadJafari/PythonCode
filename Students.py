#Student Equal#
name=input("Student Name :")
family=input("Student Family :")
Score1=input("Student Score1 : ")
Score2=input("Student Score2 : ")
Score3=input("Student Score3 : ")

Equal=int(Score1+Score2+Score3)/3
if Equal >=17:
   Status="Great" 
if Equal <17>12:
    Status="Average"
if  Equal <12:
    Status="Fail"

print(name + family + "s`Equal is" , Status)
