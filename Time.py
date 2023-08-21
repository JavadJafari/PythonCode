
def sum(t1,t2):
    result_s={}
    result_s["s"]=t1["s"]+t2["s"]
    result_s["m"]=t1["m"]+t2["m"]
    result_s["h"]=t1["h"]+t2["h"]
    # result["d"]=t1["d"]+t2["d"]
    # result["Mo"]=t1["Mo"]+t2["Mo"]
    # result["Y"]=t1["Y"]+t2["Y"]
    

    if result_s["s"]>=60:
        result_s["s"]-60
        result_s["m"]+1


    if result_s["m"]>=60:
        result_s["m"]-60
        result_s["h"]+1


    if result_s["h"]>=24:
        result_s["h"]-24
        result_s["d"]+1
    return result_s
# if result["d"]>=30:
#     result["d"]-30
#     result["Mo"]+1

# if result["Mo"]>=12:
#     result["Mo"]-12
#     result["Y"]+1
    
def div(t1,t2):
    result_d={}
    result_d["s"]=t1["s"]-t2["s"]
    result_d["m"]=t1["m"]-t2["m"]
    result_d["h"]=t1["h"]-t2["h"]
    # result["d"]=t1["d"]+t2["d"]
    # result["Mo"]=t1["Mo"]+t2["Mo"]
    # result["Y"]=t1["Y"]+t2["Y"]
    
    if result_d["s"]<=0:
        result_d["s"]+60
        result_d["m"]-1


    if result_d["m"]<=0:
        result_d["m"]+60
        result_d["h"]-1


    if result_d["h"]<=24:
        result_d["h"]+24
    
    return result_d


def show(result_s):
    print(f"'Hours:'{result_s['h']} :'Minutes:' {result_s['m']} :'Secound:' {result_s['s']}")
                        
def show(result_d):
    print(f"'Hours:'{result_d['h']} :'Minutes:' {result_d['m']} :'Secound:' {result_d['s']}") 
   


time1={"h":5 ,"m":15 , "s":14 ,}       #"Y":2023 , "Mo":6 ,"D":22 , 
time2={ "h":2 ,"m":2 , "s":2 ,}   # "Y":1993 , "Mo":6 ,"D":22 ,

result_d=div(time1,time2)
result_s=sum(time1,time2)

show(result_d)
show(result_s)




