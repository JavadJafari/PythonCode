#second_Degree-Equation
print("                              Welcome                           ")
print("                      second_Degree-Equation                    ")
print("                              By Jey                            ")
import cmath
while True:
    a=int(input("Please Enter a :"))
    b=int(input("Please Enter b :"))
    c=int(input("Please Enter c :"))

    def second_Degree_Equations():
        x1=-b-(cmath.sqrt((b**2)-4*a*c))/2*a
        x2=-b+(cmath.sqrt((b**2)-4*a*c))/2*a
        print(x1,x2)

    second_Degree_Equations()
