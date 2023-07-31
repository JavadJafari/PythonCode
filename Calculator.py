#Calculator#
while True:
   op =input( "Pls Choise Your OPration : + , - , * , / , sin , cos , tan , cot , ! , sqrt , exit :")
   import math
   num1=int(input("Enter num1 :"))
   num2=int(input("Enter num2 :"))
   if op=="+":
      result=num1+num2
   if op=="-":
      result=num1-num2
   if op=="*":
      result=num1*num2
   if op=="/":
      if num2==0:
         result="error!"
      else:
         result=num1/num2

   if op=="sin":
      num=int(input("Enter number :"))
      result= math.sin(math.radians(num))

   if op=="cos":
      num=int(input("Enter number :"))
      result= math.cos(math.radians(num))

   if op=="tan":
      num=int(input("Enter number :"))
      result= math.tan(math.radians(num))
      
   if op=="cot":
      num=int(input("Enter number :"))
      if num==0:
         result="error"
      else:
         result= 1/math.tan(math.radians(num))

   if op=="!":
       num=int(input("Enter number :"))
       result=math.factorial(math.radians(num))

   if op=="sqrt":
       num=int(input("ENter number :"))
       if num==0:
          result="error"
       else:
          result=math.sqrt(math.radians(num))
   print(result)   

    
