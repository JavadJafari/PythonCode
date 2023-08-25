#Time Convert
print("                                  Welcome                                ")
print("                        Time Convertor Application                    ")
print("                                  By Jey                                 ")
class Time:
    def __init__(self , s ,m , h):
        self.s=s
        self.m=m
        self.h=h

    def show(self):
        print(f"{self.h}:{self.m}:{self.s}")


    def Second_To_Time(self , seconds):
        self.h = seconds // 3600
        self.m = seconds // 60
        self.s = seconds % 60

    def Time_To_Seconds(self):
         result_t=(self.h*3600)+(self.m*60)+self.s
         return result_t




while True:
    user_Choise=int(input("Please Choice Your Opration >:\n Convert Second To Time Type 1: \n Convert Time To Second Type 2:\n For Exit Type 3: "))
    if user_Choise==1:
        seconds=int(input("Please Enter Seconds: "))
        t=Time(None , None , None )
        t.Second_To_Time(seconds)
        print("Result is :")
        t.show()

    elif user_Choise==2:
        second=int(input("Please Enter Second:"))
        Minutes=int(input("Please Enter Minutes:"))
        Hours=int(input("Please Enter Hours:"))
    # if 0<=second<=60 and 0<=Minutes<=60 and 0<=Hours<=24:
        t=Time(Hours , Minutes , second)
        print("Result is :")
        print(t.Time_To_Seconds(), "Seconds")


    elif user_Choise==3:
        break

    else:
        print("Try Again!!")

        
        
