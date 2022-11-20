def fractional():
    weight = [10,20,30]
    value = [60,100,120]
    WT = 50
    res = 0
    
    for pair in sorted(zip(weight,value), key= lambda x: x[1]/x[0], reverse=True):
        if WT <= 0:
            break
        if pair[0]>WT:
            res+=int(WT * (pair[1]/pair[0]))
            WT = 0
        elif pair[0]<=WT:
            res+=pair[1]
            WT -= pair[0]
    print(res)

fractional() 
   