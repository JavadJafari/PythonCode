#Deduction Opration
print("                                  Welcome                                ")
print("                       Deduction Opration Application                    ")
print("                                  By Jey                                 ")

class Frantion:
    def __init__(self , s , m):
        self.s=s
        self.m=m

    def show(self):
        print(self.s , "/" , self.m)

#Multyply/Zarb
    def mul(self ,f):
        result=Frantion(None , None)
        result.s=f1.s * f2.s
        result.m=f1.m * f2.m
        return result
#Divition/Taghsim  
    def div(self , f):
        result=Frantion(None , None)
        result.s=f1.s * f2.m
        result.m=f2.s * f1.m
        return result
#Sum/Jam
    def sum(self , f):
        result=Frantion(None , None)
        result.s=(f1.s * f2.m ) + (f2.s * f1.m)
        result.m=f1.m * f2.m
        return result

#Subtraction/Tafrigh
    def sub(self , f):
        result=Frantion(None , None)
        result.s=(f1.s * f2.m ) - (f2.s * f1.m)
        result.m=f1.m * f2.m
        return result

    
def fasele():
    print("*************************************")


 #Main_Loop/Halgheye Asli   
while True:
    user_choice=int(input("                    For Start Type 1 And for Exit Type 2 :"))
    if user_choice==1:
        f1=Frantion(int(input("Please Choice Sorat f1 :")),int(input("Please Choice Makhraj f1 :")))
        print(f"{f1.s}/{f1.m}")
        f2=Frantion(int(input("Please Choice Sorat f2 : ")) , int(input("Plesae Choice Makhraj f2: ")))
        print(f"{f2.s}/{f2.m}")

    
        fasele()
        result_mul=f1.mul(f2)
        print("Result MultyPly is :")
        result_mul.show()

        fasele()
        result_sum=f1.sum(f2)
        print("Result Sum is :")
        result_sum.show()

        fasele()
        result_div=f1.div(f2)
        print("Result Div is :")
        result_div.show()

        fasele()
        result_sub=f1.sub(f2)
        print("Result Subtracion is :")
        result_sub.show()
    elif user_choice==2:
        break














