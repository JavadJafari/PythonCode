 #Calculator#

Opration=input("Choice Your Opration ( + , - , * , / , sin , cos , tan , cot , ! , sqrt : )")
import math

if Opration=="+":
    num1=int(input("Enter num1 :"))
    num2=int(input("Enter num2 :"))
    result=num1+num2

if Opration=="-":
    num1=int(input("Enter num1 :"))
    num2=int(input("Enter num2 :"))
    result=num1-num2

if Opration=="*":
    num1=int(input("Enter num1 :"))
    num2=int(input("Enter num2 :"))
    result=num1*num2

if Opration=="/":
    num1=int(input("Enter num1 :"))
    num2=int(input("Enter num2 :"))
    if num2==int("0"):
        result="Error"
    else:
        result=num1/num2



if Opration=="sin":
    num1=int(input("Enter num1 :"))
    result=math.sin(num1)

if Opration=="cos":
    num1=int(input("Enter num1 :"))
    result=math.cos(num1)
        
if Opration=="tan":
    num1=int(input("Enter num1 :"))
    result=math.tan(num1)
        
if Opration=="cot":
    num1=int(input("Enter num1 :"))
    x=math.tan(num1)
    if x=="+":
        result="Erorr "
    else:
        result=1/math.tan(num1)
        
if Opration=="!":
    num1=int(input("Enter num1 :"))
    result=math.factorial(num1)

if Opration=="sqrt":
    num1=int(input("Enter num1 :"))
    result=math.sqrt(num1)
        
print(result)


        

