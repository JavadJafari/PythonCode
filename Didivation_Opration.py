#Creat Random List
print("                                          Wellcome                                       ")
print(" Didivation Opration")
print(" Created By 'Jey' ")

def sum(f1,f2):
    result_s={}
    result_s["s"]=(f1["s"]*f2["m"]) + (f2["s"]*f2["m"])
    result_s["m"]=f1["m"]*f2["m"]
    return result_s

def multyply(f1,f2):
    result_m={}
    result_m['s']=f1["s"]*f2["m"]
    result_m['m']=f1["m"]*f2["s"]
    return result_m

def min(f1,f2):
    result_mi={}
    result_mi["s"]=(f1["s"]*f2["m"]) - (f2["s"]*f2["m"])
    result_mi["m"]=f1["m"]*f2["m"]
    return result_mi

def div(f1,f2):
    result_mi={}
    result_mi["s"]=(f1["s"]*f2["m"])
    result_mi["m"]=f1["m"]*f2["s"]
    return result_mi

def show(r):
    print(f"{r['s']} / {r['m']}")

f1={"s":2 , "m":3}
f2={"s":5 , "m":4}


result_s=sum(f1,f2)
show(result_s)
result_m=multyply(f1,f2)
show(result_m)
result_mi=min(f1,f2)
show(result_mi)
result_d=div(f1,f2)
show(result_d)
    